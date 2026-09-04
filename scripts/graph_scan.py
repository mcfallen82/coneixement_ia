#!/usr/bin/env python3
"""Construeix i valida la capa gràfica lleugera de coneixement_ia."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI_ROOT = ROOT / "1. Wiki"
RELATIONS_PATH = ROOT / "graph" / "relations.json"
RELATION_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)

ALLOWED_RELATIONS = {
    "es_un", "part_de", "utilitza", "amplia", "depen_de", "creat_per",
    "explica", "avalua", "aplicat_a", "contrasta_amb", "exemple_de",
}
ALLOWED_STATUS = {"accepted", "candidate"}
ALLOWED_CLAIM_TYPES = {"documented", "inferred", "structural"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def node_type(path: Path) -> str:
    return {
        "1.1. autors": "author",
        "1.2. conceptes": "concept",
        "1.3. models": "model",
        "1.4. llibres": "source",
    }.get(path.parent.name, "source" if "1. Wiki/llibres" in relpath(path) else "unknown")


def node_id(path: Path, text: str) -> str:
    match = FRONTMATTER_RE.match(text)
    if match:
        found = re.search(r"^node_id:\s*['\"]?([^'\"]+)['\"]?\s*$", match.group(1), re.MULTILINE)
        if found:
            return found.group(1).strip()
    return f"{node_type(path)}:{path.stem.lower().replace(' ', '_')}"


def collect_nodes() -> tuple[dict[str, dict], dict[str, str]]:
    nodes = {}
    path_to_id = {}
    for path in sorted(WIKI_ROOT.rglob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        identifier = node_id(path, text)
        expected_type = node_type(path)
        metadata_line = next((line for line in text.splitlines() if line.startswith("node_type:")), None)
        if metadata_line is None:
            raise ValueError(f"metadades gràfiques absents: {relpath(path)}")
        metadata_type = metadata_line.split(":", 1)[1].strip().strip("'").strip('"')
        if metadata_type != expected_type:
            raise ValueError(
                f"node_type incoherent a {relpath(path)}: "
                f"{metadata_type} != {expected_type}"
            )
        if identifier in nodes:
            raise ValueError(f"node_id duplicat: {identifier}")
        nodes[identifier] = {
            "node_id": identifier,
            "node_type": node_type(path),
            "path": relpath(path),
            "title": path.stem,
        }
        path_to_id[relpath(path)] = identifier
    return nodes, path_to_id


def resolve_link(raw: str, path_to_id: dict[str, str]) -> str | None:
    """Resol un wikilink amb tolerància a variants habituals de representació.

    Primer prova la ruta canònica i després compara el nom de fitxa sense
    distingir majúscules o extensió. Això evita que la capa gràfica confongui
    una diferència de representació amb un enllaç trencat.
    """
    raw = raw.strip().replace("%20", " ").replace("\\", "/")
    candidates = [raw, raw[:-3] if raw.endswith(".md") else raw + ".md"]
    if "/" not in raw:
        candidates.extend([
            f"1. Wiki/1.1. autors/{raw}",
            f"1. Wiki/1.2. conceptes/{raw}",
            f"1. Wiki/1.3. models/{raw}",
        ])
    for candidate in candidates:
        if candidate in path_to_id:
            return path_to_id[candidate]

    wanted = raw.removesuffix(".md").split("/")[-1].casefold()
    for path, identifier in path_to_id.items():
        stem = Path(path).stem.casefold()
        if stem == wanted:
            return identifier
    return None


def load_explicit_edges(path_to_id: dict[str, str]) -> tuple[list[dict], list[str]]:
    data = json.loads(RELATIONS_PATH.read_text(encoding="utf-8"))
    errors: list[str] = []
    edges: list[dict] = []
    for index, edge in enumerate(data.get("edges", []), start=1):
        source_path = edge.get("source")
        target_path = edge.get("target")
        relation = edge.get("relation")
        status = edge.get("status", "accepted")
        claim_type = edge.get("claim_type")
        confidence = edge.get("confidence")
        if source_path not in path_to_id:
            errors.append(f"edge {index}: source inexistent: {source_path}")
        if target_path not in path_to_id:
            errors.append(f"edge {index}: target inexistent: {target_path}")
        if relation not in ALLOWED_RELATIONS:
            errors.append(f"edge {index}: relació no permesa: {relation}")
        if status not in ALLOWED_STATUS:
            errors.append(f"edge {index}: estat no permès: {status}")
        if claim_type not in ALLOWED_CLAIM_TYPES:
            errors.append(f"edge {index}: claim_type no permès: {claim_type}")
        if confidence not in ALLOWED_CONFIDENCE:
            errors.append(f"edge {index}: confiança no permesa: {confidence}")
        if status == "accepted" and claim_type == "documented" and not edge.get("evidence"):
            errors.append(f"edge {index}: relació documentada sense evidence")
        edges.append({
            **edge,
            "source": path_to_id.get(source_path, source_path),
            "target": path_to_id.get(target_path, target_path),
        })
    return edges, errors


def candidate_edges(path_to_id: dict[str, str]) -> tuple[list[dict], list[str]]:
    edges = []
    broken = []
    for path in sorted(WIKI_ROOT.rglob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        source = path_to_id[relpath(path)]
        for raw in RELATION_RE.findall(text):
            target = resolve_link(raw, path_to_id)
            if target is None:
                broken.append(f"{relpath(path)} -> [[{raw}]]")
                continue
            edges.append({
                "source": source,
                "target": target,
                "relation": "wikilink",
                "status": "candidate",
                "claim_type": "structural",
                "confidence": "low",
            })
    return edges, broken


def build_graph() -> tuple[dict, list[str]]:
    nodes, path_to_id = collect_nodes()
    explicit, errors = load_explicit_edges(path_to_id)
    candidates, broken = candidate_edges(path_to_id)
    return {
        "version": 1,
        "source": "Markdown",
        "nodes": list(nodes.values()),
        "edges": explicit + candidates,
        "stats": {
            "nodes": len(nodes),
            "accepted_edges": len(explicit),
            "candidate_edges": len(candidates),
            "broken_wikilinks": len(broken),
        },
        "broken_wikilinks": broken,
    }, errors


def print_stats(graph: dict) -> None:
    degrees = Counter()
    adjacency: dict[str, set[str]] = {}
    for edge in graph["edges"]:
        degrees[edge["source"]] += 1
        degrees[edge["target"]] += 1
        adjacency.setdefault(edge["source"], set()).add(edge["target"])
        adjacency.setdefault(edge["target"], set()).add(edge["source"])
    components = 0
    unseen = set(adjacency)
    while unseen:
        components += 1
        start = unseen.pop()
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for neighbour in adjacency.get(current, set()):
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    queue.append(neighbour)
    print(f"NODES: {graph['stats']['nodes']}")
    print(f"ACCEPTED_EDGES: {graph['stats']['accepted_edges']}")
    print(f"CANDIDATE_EDGES: {graph['stats']['candidate_edges']}")
    print(f"BROKEN_WIKILINKS: {graph['stats']['broken_wikilinks']}")
    print(f"CONNECTED_COMPONENTS: {components}")
    print("HUBS:")
    for identifier, degree in degrees.most_common(5):
        print(f"  {identifier}: {degree}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="valida el registre i els enllaços")
    parser.add_argument("--stats", action="store_true", help="mostra estadístiques")
    parser.add_argument("--output", type=Path, help="escriu una instantània JSON")
    args = parser.parse_args()

    try:
        graph, errors = build_graph()
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 1

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.stats:
        print_stats(graph)

    if args.check or not (args.stats or args.output):
        for error in errors:
            print(f"ERROR: {error}")
        for broken in graph["broken_wikilinks"]:
            print(f"WARN: wikilink sense destinació: {broken}")
        print(f"GRAPH CHECK — errors: {len(errors)}; wikilinks trencats: {len(graph['broken_wikilinks'])}")
        print("FAIL" if errors else "PASS")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
