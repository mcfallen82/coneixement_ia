#!/usr/bin/env python3
"""Proposa fitxes relacionades per revisar després d'una ingesta.

Adaptació lleugera d'una fase d'A-MEM: el rànquing és lèxic, no un
embedding semàntic, i mai no escriu ni accepta enllaços automàticament.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
WORD_RE = re.compile(r"[^\W_]+", re.UNICODE)
STOPWORDS = {
    "amb", "com", "del", "dels", "les", "els", "una", "unes", "uns",
    "per", "que", "són", "una", "the", "and", "for", "with", "from",
    "this", "that", "sobre", "quan", "aquest", "aquesta", "aquests",
    "aquestes", "model", "models", "concepte", "conceptes", "font",
    "fonts", "wiki", "relacions", "relació", "aplicacions", "exemple",
    "important", "funcionament", "limitacions", "errors", "status",
    "created", "updated", "sources", "http", "https", "github", "arxiv",
    "llm", "mem", "agentic", "pot", "també", "dels", "així",
    "però", "més", "fer", "seva", "seves", "seus", "després",
}


def parse_note(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError(f"Frontmatter absent: {path}")
    meta = yaml.safe_load(match.group(1)) or {}
    # Les fonts i els wikilinks no han d'inflar el rànquing per noms d'URL o rutes.
    body = re.split(r"(?m)^##\s+Fonts?\s*$", text[match.end():], maxsplit=1)[0]
    body = LINK_RE.sub(" ", body)
    body = re.sub(r"https?://\S+", " ", body)
    body = re.sub(r"(?m)^##?\s+.*$", " ", body)
    title = str(meta.get("title") or path.stem)
    tags = " ".join(str(tag) for tag in meta.get("tags", []))
    return {
        "path": path,
        "text": text,
        "title": title,
        "node_id": str(meta.get("node_id") or ""),
        "terms": tokenize(body + " " + (title + " ") * 3 + (tags + " ") * 2),
    }


def tokenize(text: str) -> Counter:
    return Counter(
        token for token in (word.casefold() for word in WORD_RE.findall(text))
        if len(token) >= 3 and token not in STOPWORDS and not token.isdigit()
    )


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    common = a.keys() & b.keys()
    dot = sum(a[word] * b[word] for word in common)
    norm_a = math.sqrt(sum(weight * weight for weight in a.values()))
    norm_b = math.sqrt(sum(weight * weight for weight in b.values()))
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0


def rank_candidates(note_path: Path, wiki_root: Path, top_k: int = 5) -> list[dict]:
    """Retorna candidates de lectura; no actualitza cap fitxa ni el graf."""
    paths = sorted(p for p in wiki_root.rglob("*.md") if p.name != "README.md")
    if note_path not in paths:
        raise ValueError("La fitxa d'entrada ha de ser dins de la wiki")
    notes = [parse_note(path) for path in paths]
    source = next(note for note in notes if note["path"] == note_path)
    frequency = Counter(word for note in notes for word in note["terms"])
    count = len(notes)

    def vector(note: dict) -> dict[str, float]:
        return {
            word: (1 + math.log(n)) * (1 + math.log((count + 1) / (frequency[word] + 1)))
            for word, n in note["terms"].items()
        }

    source_vector = vector(source)
    existing = {link.removesuffix(".md").casefold() for link in LINK_RE.findall(source["text"])}
    stem_counts = Counter(path.stem.casefold() for path in paths)
    ranked = []
    for candidate in notes:
        if candidate is source:
            continue
        shared = source["terms"].keys() & candidate["terms"].keys()
        if not shared:
            continue
        score = cosine(source_vector, vector(candidate))
        ranked.append({
            "path": candidate["path"].relative_to(wiki_root.parent).as_posix(),
            "node_id": candidate["node_id"],
            "title": candidate["title"],
            "score": round(score, 4),
            "shared_terms": sorted(shared, key=lambda word: (-source["terms"][word] - candidate["terms"][word], word))[:8],
            "already_linked": (
                candidate["path"].relative_to(wiki_root.parent).with_suffix("").as_posix().casefold() in existing
                or (stem_counts[candidate["path"].stem.casefold()] == 1
                    and candidate["path"].stem.casefold() in existing)
            ),
        })
    return sorted(ranked, key=lambda item: (-item["score"], item["path"]))[:top_k]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--note", required=True, help="Ruta d'una fitxa Markdown de la wiki")
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()
    if args.top_k < 1:
        parser.error("--top-k ha de ser positiu")
    note = (ROOT / args.note).resolve()
    wiki = ROOT / "1. Wiki"
    if not note.is_relative_to(wiki) or not note.is_file() or note.suffix != ".md":
        parser.error("--note ha d'apuntar a una fitxa Markdown existent dins de 1. Wiki")
    print(json.dumps({
        "source": note.relative_to(ROOT).as_posix(),
        "method": "tf-idf lexic; candidates per a revisio, no relacions validades",
        "candidates": rank_candidates(note, wiki, args.top_k),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
