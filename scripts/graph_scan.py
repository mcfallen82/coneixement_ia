#!/usr/bin/env python3
"""Construeix i valida la capa gràfica lleugera de coneixement_ia."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, deque
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WIKI_ROOT = ROOT / "1. Wiki"
RELATIONS_PATH = ROOT / "graph" / "relations.json"
VOCABULARY_PATH = ROOT / "graph" / "relation-vocabulary.yaml"
RELATION_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def node_type(path: Path) -> str:
    return {
        "1.1. autors": "author",
        "1.2. conceptes": "concept",
        "1.3. models": "model",
        "1.4. llibres": "source",
    }.get(path.parent.name, "unknown")


def node_id(path: Path, text: str) -> str:
    match = FRONTMATTER_RE.match(text)
    if match:
        found = re.search(
            r"^node_id:\s*['\"]?([^'\"]+)['\"]?\s*$",
            match.group(1),
            re.MULTILINE,
        )
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
        metadata_line = next(
            (line for line in text.splitlines() if line.startswith("node_type:")),
            None,
        )
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
            "node_type": expected_type,
            "path": relpath(path),
            "title": path.stem,
        }
        path_to_id[relpath(path)] = identifier
    return nodes, path_to_id


def resolve_link(raw: str, path_to_id: dict[str, str]) -> tuple[str | None, list[str]]:
    """Resol un wikilink amb tolerància a variants habituals."""
    raw = raw.strip().replace("%20", " ").replace("\\", "/")
    candidates = [raw, raw[:-3] if raw.endswith(".md") else raw + ".md"]
    if "/" not in raw:
        candidates.extend(
            [
                f"1. Wiki/1.1. autors/{raw}",
                f"1. Wiki/1.2. conceptes/{raw}",
                f"1. Wiki/1.3. models/{raw}",
                f"1. Wiki/1.4. llibres/{raw}",
            ]
        )
    for candidate in candidates:
        if candidate in path_to_id:
            return path_to_id[candidate], []

    wanted = raw.removesuffix(".md").split("/")[-1].casefold()
    matches = [
        identifier
        for path, identifier in path_to_id.items()
        if Path(path).stem.casefold() == wanted
    ]
    if len(matches) == 1:
        return matches[0], []
    return None, sorted(matches)


def load_vocabulary() -> tuple[dict[str, set[str]], list[str]]:
    """Carrega el vocabulari canònic i valida les relacions inverses."""
    data = yaml.safe_load(VOCABULARY_PATH.read_text(encoding="utf-8")) or {}
    errors: list[str] = []
    relation_defs = data.get("relations", [])
    if not isinstance(relation_defs, list):
        raise ValueError("relation-vocabulary.yaml: relations ha de ser una llista")

    relation_ids = []
    inverse_by_relation = {}
    for index, item in enumerate(relation_defs, start=1):
        if not isinstance(item, dict) or not item.get("id"):
            errors.append(f"vocabulari {index}: definició de relació invàlida")
            continue
        relation = str(item["id"])
        if relation in relation_ids:
            errors.append(f"vocabulari: relació duplicada: {relation}")
        relation_ids.append(relation)
        inverse_by_relation[relation] = item.get("inverse")

    allowed_relations = set(relation_ids)
    for relation, inverse in inverse_by_relation.items():
        if not isinstance(inverse, str) or not inverse:
            errors.append(f"vocabulari: inversa invàlida per {relation}")
        else:
            allowed_relations.add(inverse)

    rules = data.get("rules", {}) or {}
    vocabulary = {
        "relations": allowed_relations,
        "status": set(rules.get("allowed_status", [])),
        "claim_type": set(rules.get("allowed_claim_type", [])),
        "confidence": set(rules.get("allowed_confidence", [])),
    }
    for key, values in vocabulary.items():
        if not values:
            errors.append(f"vocabulari: conjunt buit: {key}")
    return vocabulary, errors


def validate_evidence(index: int, edge: dict, errors: list[str]) -> None:
    evidence = edge.get("evidence", [])
    if edge.get("status", "accepted") == "accepted" and edge.get("claim_type") == "documented" and not evidence:
        errors.append(f"edge {index}: relació documentada sense evidence")
        return
    if evidence and not isinstance(evidence, list):
        errors.append(f"edge {index}: evidence ha de ser una llista")
        return
    for item in evidence:
        if not isinstance(item, str) or not item.strip():
            errors.append(f"edge {index}: evidence conté un valor invàlid")
        elif item.startswith(("https://", "http://")):
            continue
        elif not (ROOT / item).is_file():
            errors.append(f"edge {index}: evidence interna inexistent: {item}")


def load_explicit_edges(
    path_to_id: dict[str, str], vocabulary: dict[str, set[str]]
) -> tuple[list[dict], list[str]]:
    data = json.loads(RELATIONS_PATH.read_text(encoding="utf-8"))
    errors: list[str] = []
    edges: list[dict] = []
    seen: set[tuple[str, str, str]] = set()
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
        if relation not in vocabulary["relations"]:
            errors.append(f"edge {index}: relació no permesa: {relation}")
        if status not in vocabulary["status"]:
            errors.append(f"edge {index}: estat no permès: {status}")
        if claim_type not in vocabulary["claim_type"]:
            errors.append(f"edge {index}: claim_type no permès: {claim_type}")
        if confidence not in vocabulary["confidence"]:
            errors.append(f"edge {index}: confiança no permesa: {confidence}")
        validate_evidence(index, edge, errors)

        key = (str(source_path), str(target_path), str(relation))
        if key in seen:
            errors.append(f"edge {index}: relació acceptada duplicada: {key}")
        seen.add(key)
        edges.append(
            {
                **edge,
                "source": path_to_id.get(source_path, source_path),
                "target": path_to_id.get(target_path, target_path),
            }
        )
    return edges, errors


def candidate_edges(
    path_to_id: dict[str, str]
) -> tuple[list[dict], list[str], list[str]]:
    """Converteix wikilinks en parelles úniques i conserva la procedència."""
    candidates: dict[tuple[str, str], dict] = {}
    broken: set[str] = set()
    ambiguous: set[str] = set()
    for path in sorted(WIKI_ROOT.rglob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        source = path_to_id[relpath(path)]
        for line_number, line in enumerate(text.splitlines(), start=1):
            for raw in RELATION_RE.findall(line):
                target, matches = resolve_link(raw, path_to_id)
                if target is None:
                    if matches:
                        options = ", ".join(matches)
                        ambiguous.add(
                            f"{relpath(path)} -> [[{raw}]] (opcions: {options})"
                        )
                    else:
                        broken.add(f"{relpath(path)} -> [[{raw}]]")
                    continue
                key = (source, target)
                origin = f"{relpath(path)}#L{line_number}"
                if key not in candidates:
                    candidates[key] = {
                        "source": source,
                        "target": target,
                        "relation": "wikilink",
                        "status": "candidate",
                        "claim_type": "structural",
                        "confidence": "low",
                        "occurrences": 0,
                        "origins": [],
                    }
                candidates[key]["occurrences"] += 1
                candidates[key]["origins"].append(origin)
    return list(candidates.values()), sorted(broken), sorted(ambiguous)


def build_graph() -> tuple[dict, list[str]]:
    nodes, path_to_id = collect_nodes()
    vocabulary, vocabulary_errors = load_vocabulary()
    explicit, edge_errors = load_explicit_edges(path_to_id, vocabulary)
    candidates, broken, ambiguous = candidate_edges(path_to_id)
    accepted_nodes = {
        node_id
        for edge in explicit
        for node_id in (edge["source"], edge["target"])
        if node_id in nodes
    }
    return {
        "version": 2,
        "source": "Markdown",
        "nodes": list(nodes.values()),
        "edges": explicit + candidates,
        "stats": {
            "nodes": len(nodes),
            "accepted_edges": len(explicit),
            "accepted_nodes": len(accepted_nodes),
            "accepted_coverage_pct": round(100 * len(accepted_nodes) / len(nodes), 1) if nodes else 0,
            "candidate_edges": len(candidates),
            "candidate_occurrences": sum(edge["occurrences"] for edge in candidates),
            "broken_wikilinks": len(broken),
            "ambiguous_wikilinks": len(ambiguous),
        },
        "broken_wikilinks": broken,
        "ambiguous_wikilinks": ambiguous,
    }, vocabulary_errors + edge_errors


def print_stats(graph: dict) -> None:
    degrees = Counter()
    adjacency: dict[str, set[str]] = {
        node["node_id"]: set() for node in graph["nodes"]
    }
    for edge in graph["edges"]:
        degrees[edge["source"]] += 1
        degrees[edge["target"]] += 1
        adjacency[edge["source"]].add(edge["target"])
        adjacency[edge["target"]].add(edge["source"])
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
    stats = graph["stats"]
    print(f"NODES: {stats['nodes']}")
    print(f"ACCEPTED_EDGES: {stats['accepted_edges']}")
    print(f"ACCEPTED_NODES: {stats['accepted_nodes']}")
    print(f"ACCEPTED_COVERAGE_PCT: {stats['accepted_coverage_pct']}")
    print(f"CANDIDATE_EDGES: {stats['candidate_edges']}")
    print(f"CANDIDATE_OCCURRENCES: {stats['candidate_occurrences']}")
    print(f"BROKEN_WIKILINKS: {stats['broken_wikilinks']}")
    print(f"AMBIGUOUS_WIKILINKS: {stats['ambiguous_wikilinks']}")
    print(f"CONNECTED_COMPONENTS: {components}")
    print("HUBS:")
    for identifier, degree in degrees.most_common(5):
        print(f"  {identifier}: {degree}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="valida el registre i els enllaços")
    parser.add_argument("--strict", action="store_true", help="tracta wikilinks trencats com a errors")
    parser.add_argument("--stats", action="store_true", help="mostra estadístiques")
    parser.add_argument("--output", type=Path, help="escriu una instantània JSON")
    args = parser.parse_args()

    try:
        graph, errors = build_graph()
    except (OSError, json.JSONDecodeError, yaml.YAMLError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 1

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(graph, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    if args.stats:
        print_stats(graph)
    if args.check or not (args.stats or args.output):
        for error in errors:
            print(f"ERROR: {error}")
        for broken in graph["broken_wikilinks"]:
            print(f"WARN: wikilink sense destinació: {broken}")
        for ambiguous in graph["ambiguous_wikilinks"]:
            print(f"WARN: wikilink ambigu: {ambiguous}")
        unresolved = len(graph["broken_wikilinks"]) + len(graph["ambiguous_wikilinks"])
        strict_failures = unresolved if args.strict else 0
        print(
            "GRAPH CHECK — "
            f"errors: {len(errors)}; "
            f"wikilinks trencats: {len(graph['broken_wikilinks'])}; "
            f"wikilinks ambigus: {len(graph['ambiguous_wikilinks'])}"
        )
        print("FAIL" if errors or strict_failures else "PASS")
    return 1 if errors or (args.strict and graph["broken_wikilinks"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
