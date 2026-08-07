#!/usr/bin/env python3
"""Auditoria determinista de l’arquitectura i les fitxes de ia_knowledge."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FAIL: PyYAML és necessari; executa: python -m pip install pyyaml")
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DIRS = [
    "0. Raw", "0. Raw/0.1. llibres", "0. Raw/0.2.",
    "1. Wiki", "1. Wiki/1.1. autors", "1. Wiki/1.2. conceptes",
    "1. Wiki/1.3. models", "2. Skills", "3. Dashboards",
    "4. Templates", "4. Templates/90.1. templates_fitxes",
    "4. Templates/90.2. docs_support",
]
REQUIRED_FILES = [
    "AGENTS.md", "README.md", "index.md", "log.md", "hot.md",
    ".manifest.json", "2. Skills/README.md", "scripts/wiki_lint.py",
]
CATEGORY_BY_DIR = {
    "1.1. autors": "autors",
    "1.2. conceptes": "conceptes",
    "1.3. models": "models",
}
COMMON_FIELDS = {"title", "category", "tags", "sources", "status", "created", "updated"}
LEGACY_PATTERNS = [
    (re.compile(r"^autor\s*:", re.MULTILINE), "camp antic autor:"),
    (re.compile(r"^estat\s*:", re.MULTILINE), "camp antic estat:"),
    (re.compile(r"concepts/|entities/|references/"), "ruta antiga"),
]
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


class Audit:
    def __init__(self, strict: bool) -> None:
        self.strict = strict
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        if self.strict:
            self.errors.append(message)
        else:
            self.warnings.append(message)


def read_frontmatter(path: Path, audit: Audit):
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    if not text.startswith("---\n"):
        audit.warning(f"{rel}: falta frontmatter; fitxa pendent de normalització")
        return None, text
    match = re.match(r"^---\n(.*?)\n---\n?", text, re.DOTALL)
    if not match:
        audit.error(f"{rel}: frontmatter no tancat")
        return None, text
    if re.search(r"\n---\n\s*---\n", text[match.end():]):
        audit.error(f"{rel}: frontmatter duplicat o bloc YAML addicional")

    try:
        data = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        audit.error(f"{rel}: YAML invàlid ({exc})")
        return None, text
    if not isinstance(data, dict):
        audit.error(f"{rel}: frontmatter no és un mapa")
        return None, text
    return data, text


def target_candidates(raw: str):
    raw = raw.strip().replace("%20", " ")
    if raw.startswith(("http://", "https://")):
        return []
    candidates = [raw, raw[:-3] if raw.endswith(".md") else raw + ".md"]
    if "/" not in raw:
        candidates.extend([
            f"1. Wiki/1.1. autors/{raw}", f"1. Wiki/1.2. conceptes/{raw}",
            f"1. Wiki/1.3. models/{raw}", f"2. Skills/{raw}",
            f"3. Dashboards/{raw}", f"4. Templates/{raw}",
        ])
    return candidates


def validate_links(path: Path, audit: Audit, all_files: set[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for raw in WIKILINK_RE.findall(text):
        candidates = target_candidates(raw)
        if candidates and not any(candidate in all_files for candidate in candidates):
            audit.warning(f"{path.relative_to(ROOT)}: wikilink sense destinació: [[{raw}]]")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true",
                        help="converteix totes les advertències en errors")
    args = parser.parse_args()
    audit = Audit(strict=args.strict)

    for directory in REQUIRED_DIRS:
        if not (ROOT / directory).is_dir():
            audit.error(f"falta carpeta obligatòria: {directory}")
    for filename in REQUIRED_FILES:
        if not (ROOT / filename).is_file():
            audit.error(f"falta fitxer obligatori: {filename}")

    markdown_files = {
        str(path.relative_to(ROOT)).replace("\\", "/")
        for path in ROOT.rglob("*.md") if ".git" not in path.parts
    }
    permanent = []
    titles: defaultdict[str, list[str]] = defaultdict(list)

    for directory, expected_category in CATEGORY_BY_DIR.items():
        folder = ROOT / "1. Wiki" / directory
        if not folder.is_dir():
            continue
        for path in sorted(folder.glob("*.md")):
            if path.name == "README.md":
                continue
            data, _ = read_frontmatter(path, audit)
            if data is None:
                continue
            rel = str(path.relative_to(ROOT)).replace("\\", "/")
            permanent.append(path)
            missing = COMMON_FIELDS - set(data)
            for field in sorted(missing):
                audit.warning(f"{rel}: falta camp {field}")
            if "category" in data and data.get("category") != expected_category:
                audit.error(f"{rel}: category={data.get('category')!r}, esperat {expected_category!r}")
            if "sources" in data and not isinstance(data.get("sources"), list):
                audit.warning(f"{rel}: sources ha de ser una llista")
            if "tags" in data and not isinstance(data.get("tags"), list):
                audit.warning(f"{rel}: tags ha de ser una llista")
            for relation_field in ("related_concepts", "related_models"):
                if relation_field in data and not isinstance(data.get(relation_field), list):
                    audit.error(f"{rel}: {relation_field} ha de ser una llista")
                elif relation_field in data:
                    invalid = [item for item in data[relation_field] if not isinstance(item, str)]
                    if invalid:
                        audit.error(f"{rel}: {relation_field} ha de contenir cadenes, no estructures YAML imbricades")
            if path.parent.name == "1.3. models":
                for field in ("model_family", "architecture"):
                    if field not in data:
                        audit.warning(f"{rel}: falta camp de model {field}")
            if data.get("status") == "draft":
                audit.warning(f"{rel}: fitxa en estat draft")
            if "sources" in data and not data.get("sources"):
                audit.warning(f"{rel}: fitxa sense fonts")
            title = str(data.get("title", "")).strip().lower()
            if title:
                titles[expected_category].append(rel + " :: " + title)
            validate_links(path, audit, markdown_files)

    for category, entries in titles.items():
        grouped: defaultdict[str, list[str]] = defaultdict(list)
        for entry in entries:
            rel, title = entry.split(" :: ", 1)
            grouped[title].append(rel)
        for title, paths in grouped.items():
            if len(paths) > 1:
                audit.error(f"títol duplicat a {category}: {title} ({', '.join(paths)})")

    legacy_scope = list(permanent)
    template_dir = ROOT / "4. Templates/90.1. templates_fitxes"
    if template_dir.is_dir():
        legacy_scope.extend(path for path in template_dir.glob("*.md"))
    for path in legacy_scope:
        text = path.read_text(encoding="utf-8")
        for pattern, label in LEGACY_PATTERNS:
            if pattern.search(text):
                audit.warning(f"{path.relative_to(ROOT)}: {label}")

    manifest_path = ROOT / ".manifest.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            audit.error(f".manifest.json: JSON invàlid ({exc})")
            manifest = {}
        if not isinstance(manifest, dict):
            audit.error(".manifest.json: l’arrel ha de ser un objecte")
        for operation in manifest.get("operations", []):
            for source in operation.get("ingested_sources", []):
                source_path = source.get("path")
                if source_path and not (ROOT / source_path).exists():
                    audit.error(f".manifest.json: ruta de font inexistent: {source_path}")
            for key in ("pages_created", "pages_updated"):
                for page in operation.get(key, []):
                    if not (ROOT / page).exists():
                        audit.error(f".manifest.json: pàgina inexistent a {key}: {page}")

    print(f"WIKI LINT — {date.today().isoformat()}")
    print(f"Fitxes amb frontmatter revisades: {len(permanent)}")
    print(f"Errors bloquejants: {len(audit.errors)}")
    print(f"Advertiments de normalització: {len(audit.warnings)}")
    for item in audit.errors:
        print(f"ERROR: {item}")
    for item in audit.warnings:
        print(f"WARN: {item}")
    print("FAIL" if audit.errors else "PASS")
    return 1 if audit.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
