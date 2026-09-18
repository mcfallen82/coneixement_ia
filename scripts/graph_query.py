#!/usr/bin/env python3
"""Consulta determinista de la capa gràfica de coneixement_ia."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

from graph_scan import build_graph


class QueryError(ValueError):
    """Error de consulta comprensible per a l'usuari."""


class GraphQuery:
    """Índex en memòria per consultar nodes, arestes, camins i subgrafs."""

    def __init__(self, graph: dict[str, Any], include_candidates: bool = False) -> None:
        self.nodes = {node["node_id"]: node for node in graph["nodes"]}
        self.edges = [
            edge
            for edge in graph["edges"]
            if include_candidates or edge.get("status") == "accepted"
        ]
        self.outgoing: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.incoming: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.aliases: dict[str, set[str]] = defaultdict(set)

        for node_id, node in self.nodes.items():
            path = node["path"]
            aliases = {
                node_id,
                node["title"],
                path,
                path.removesuffix(".md"),
                Path(path).stem,
            }
            for alias in aliases:
                self.aliases[self._normalise(alias)].add(node_id)

        for edge in self.edges:
            self.outgoing[edge["source"]].append(edge)
            self.incoming[edge["target"]].append(edge)

        key = lambda edge: (edge["relation"], edge["source"], edge["target"])
        for edge_list in (*self.outgoing.values(), *self.incoming.values()):
            edge_list.sort(key=key)

    @staticmethod
    def _normalise(value: str) -> str:
        return value.strip().replace("\\", "/").casefold()

    def resolve(self, query: str) -> str:
        """Resol un node per node_id, títol, nom de fitxer o ruta."""
        matches = self.aliases.get(self._normalise(query), set())
        if not matches:
            raise QueryError(f"node no trobat: {query}")
        if len(matches) > 1:
            options = ", ".join(sorted(matches))
            raise QueryError(f"node ambigu: {query}. Opcions: {options}")
        return next(iter(matches))

    def neighbours(self, node: str) -> list[dict[str, Any]]:
        node_id = self.resolve(node)
        result = []
        for edge in self.outgoing.get(node_id, []):
            result.append({
                "direction": "outgoing",
                "node": self.nodes[edge["target"]],
                "edge": edge,
            })
        for edge in self.incoming.get(node_id, []):
            result.append({
                "direction": "incoming",
                "node": self.nodes[edge["source"]],
                "edge": edge,
            })
        return result

    def path(self, source: str, target: str, max_depth: int = 3) -> dict[str, Any] | None:
        """Troba el camí dirigit més curt mitjançant BFS."""
        if max_depth < 1:
            raise QueryError("max-depth ha de ser com a mínim 1")
        source_id = self.resolve(source)
        target_id = self.resolve(target)
        if source_id == target_id:
            return {"nodes": [self.nodes[source_id]], "edges": []}

        queue = deque([(source_id, [], [source_id])])
        best_depth = {source_id: 0}
        while queue:
            current, path_edges, path_nodes = queue.popleft()
            if len(path_edges) >= max_depth:
                continue
            for edge in self.outgoing.get(current, []):
                neighbour = edge["target"]
                next_edges = [*path_edges, edge]
                next_nodes = [*path_nodes, neighbour]
                if neighbour == target_id:
                    return {
                        "nodes": [self.nodes[node_id] for node_id in next_nodes],
                        "edges": next_edges,
                    }
                depth = len(next_edges)
                if depth < best_depth.get(neighbour, max_depth + 1):
                    best_depth[neighbour] = depth
                    queue.append((neighbour, next_edges, next_nodes))
        return None

    def subgraph(self, node: str, depth: int = 1) -> dict[str, Any]:
        """Extreu el veïnat no dirigit fins a la profunditat indicada."""
        if depth < 0:
            raise QueryError("depth no pot ser negatiu")
        start = self.resolve(node)
        distances = {start: 0}
        queue = deque([start])
        while queue:
            current = queue.popleft()
            if distances[current] >= depth:
                continue
            incident = [*self.outgoing.get(current, []), *self.incoming.get(current, [])]
            for edge in incident:
                neighbour = edge["target"] if edge["source"] == current else edge["source"]
                if neighbour not in distances:
                    distances[neighbour] = distances[current] + 1
                    queue.append(neighbour)

        selected = set(distances)
        nodes = [
            {**self.nodes[node_id], "distance": distances[node_id]}
            for node_id in sorted(selected, key=lambda item: (distances[item], item))
        ]
        edges = [
            edge for edge in self.edges
            if edge["source"] in selected and edge["target"] in selected
        ]
        return {"root": self.nodes[start], "depth": depth, "nodes": nodes, "edges": edges}

    def explain_edge(self, source: str, target: str) -> list[dict[str, Any]]:
        """Retorna les relacions directes i la seva procedència en ambdós sentits."""
        source_id = self.resolve(source)
        target_id = self.resolve(target)
        explanations = []
        for edge in self.edges:
            if edge["source"] == source_id and edge["target"] == target_id:
                explanations.append({"direction": "forward", "edge": edge})
            elif edge["source"] == target_id and edge["target"] == source_id:
                explanations.append({"direction": "reverse", "edge": edge})
        return explanations


def add_output_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--include-candidates",
        action="store_true",
        help="inclou wikilinks candidats; per defecte només usa relacions acceptades",
    )
    parser.add_argument("--json", action="store_true", help="retorna JSON")


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Motor GraphQA local i determinista de coneixement_ia"
    )
    commands = parser.add_subparsers(dest="command", required=True)

    neighbours = commands.add_parser("neighbors", help="mostra relacions entrants i sortints")
    neighbours.add_argument("node")
    add_output_options(neighbours)

    path = commands.add_parser("path", help="troba el camí dirigit més curt")
    path.add_argument("source")
    path.add_argument("target")
    path.add_argument("--max-depth", type=int, default=3)
    add_output_options(path)

    subgraph = commands.add_parser("subgraph", help="extreu el subgraf al voltant d'un node")
    subgraph.add_argument("node")
    subgraph.add_argument("--depth", type=int, default=1)
    add_output_options(subgraph)

    explain = commands.add_parser("explain-edge", help="explica una relació directa")
    explain.add_argument("source")
    explain.add_argument("target")
    add_output_options(explain)
    return parser


def label(node: dict[str, Any]) -> str:
    return f"{node['title']} [{node['node_id']}]"


def print_neighbours(query: GraphQuery, node: str, result: list[dict[str, Any]]) -> None:
    node_id = query.resolve(node)
    print(label(query.nodes[node_id]))
    if not result:
        print("  cap relació")
        return
    for item in result:
        edge = item["edge"]
        arrow = "→" if item["direction"] == "outgoing" else "←"
        print(f"  {arrow} {edge['relation']} {arrow} {label(item['node'])}")


def print_path(result: dict[str, Any] | None) -> None:
    if result is None:
        print("Cap camí trobat.")
        return
    print(label(result["nodes"][0]))
    for edge, node in zip(result["edges"], result["nodes"][1:]):
        print(f"  └─ {edge['relation']} → {label(node)}")


def print_subgraph(result: dict[str, Any]) -> None:
    print(f"Subgraf de {label(result['root'])} — profunditat {result['depth']}")
    print("Nodes:")
    for node in result["nodes"]:
        print(f"  [{node['distance']}] {label(node)}")
    print("Relacions:")
    for edge in result["edges"]:
        print(f"  {edge['source']} ─{edge['relation']}→ {edge['target']}")


def print_explanations(result: list[dict[str, Any]]) -> None:
    if not result:
        print("No hi ha cap relació directa.")
        return
    for item in result:
        edge = item["edge"]
        print(f"{edge['source']} ─{edge['relation']}→ {edge['target']}")
        print(f"  direcció: {item['direction']}")
        print(f"  status: {edge.get('status', 'desconegut')}")
        print(f"  claim_type: {edge.get('claim_type', 'desconegut')}")
        print(f"  confidence: {edge.get('confidence', 'desconeguda')}")
        if edge.get("note"):
            print(f"  nota: {edge['note']}")
        for evidence in edge.get("evidence", []):
            print(f"  evidence: {evidence}")


def main() -> int:
    args = make_parser().parse_args()
    try:
        graph, errors = build_graph()
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        query = GraphQuery(graph, include_candidates=args.include_candidates)
        if args.command == "neighbors":
            result = query.neighbours(args.node)
        elif args.command == "path":
            result = query.path(args.source, args.target, args.max_depth)
        elif args.command == "subgraph":
            result = query.subgraph(args.node, args.depth)
        else:
            result = query.explain_edge(args.source, args.target)
    except (OSError, json.JSONDecodeError, QueryError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif args.command == "neighbors":
        print_neighbours(query, args.node, result)
    elif args.command == "path":
        print_path(result)
    elif args.command == "subgraph":
        print_subgraph(result)
    else:
        print_explanations(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
