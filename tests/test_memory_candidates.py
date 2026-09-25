"""Proves del rànquing de lectura sense mutacions sobre una wiki petita."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from memory_candidates import rank_candidates  # noqa: E402


class MemoryCandidatesTests(unittest.TestCase):
    def test_ranks_relevant_note_and_does_not_modify_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            wiki = Path(directory) / "1. Wiki"
            wiki.mkdir()
            source = wiki / "new.md"
            relevant = wiki / "related.md"
            other = wiki / "other.md"
            source.write_text("---\ntitle: Grafs de memòria\nnode_id: concept:new\ntags: [memoria]\n---\nEls grafs connecten records i conceptes de la memòria.\n", encoding="utf-8")
            relevant.write_text("---\ntitle: Memòria amb grafs\nnode_id: concept:related\ntags: [memoria]\n---\nEls grafs relacionen conceptes i records.\n", encoding="utf-8")
            other.write_text("---\ntitle: Cuina italiana\nnode_id: concept:other\ntags: [cuina]\n---\nLa pasta necessita aigua i sal.\n", encoding="utf-8")
            before = {path: path.read_bytes() for path in (source, relevant, other)}

            result = rank_candidates(source, wiki, top_k=2)

            self.assertEqual([item["path"] for item in result], ["1. Wiki/related.md"])
            self.assertGreater(result[0]["score"], 0)
            self.assertFalse(result[0]["already_linked"])
            self.assertEqual(before, {path: path.read_bytes() for path in before})

    def test_ambiguous_basename_requires_explicit_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            wiki = Path(directory) / "1. Wiki"
            (wiki / "conceptes").mkdir(parents=True)
            (wiki / "models").mkdir()
            source = wiki / "new.md"
            source.write_text("---\ntitle: Memòria\n---\nRecord relacionat amb [[1. Wiki/conceptes/nota]].\nNotes sobre memòria.\n", encoding="utf-8")
            for folder in ("conceptes", "models"):
                (wiki / folder / "nota.md").write_text("---\ntitle: Nota\n---\nNotes sobre memòria i records.\n", encoding="utf-8")

            result = rank_candidates(source, wiki)
            linked = {item["path"]: item["already_linked"] for item in result}
            self.assertTrue(linked["1. Wiki/conceptes/nota.md"])
            self.assertFalse(linked["1. Wiki/models/nota.md"])


if __name__ == "__main__":
    unittest.main()
