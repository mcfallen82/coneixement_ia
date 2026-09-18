"""Proves d'integració de la capa gràfica sobre la wiki real."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from graph_scan import build_graph, load_vocabulary  # noqa: E402


class GraphScanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.graph, cls.errors = build_graph()

    def test_real_graph_has_no_validation_errors(self) -> None:
        self.assertEqual(self.errors, [])
        self.assertEqual(self.graph["broken_wikilinks"], [])
        self.assertEqual(self.graph["ambiguous_wikilinks"], [])

    def test_candidate_edges_are_unique_and_keep_occurrences(self) -> None:
        candidates = [
            edge for edge in self.graph["edges"] if edge["status"] == "candidate"
        ]
        keys = {
            (edge["source"], edge["target"], edge["relation"])
            for edge in candidates
        }
        self.assertEqual(len(candidates), len(keys))
        for edge in candidates:
            self.assertEqual(edge["occurrences"], len(edge["origins"]))
            self.assertGreaterEqual(edge["occurrences"], 1)

    def test_accepted_edges_reference_existing_nodes(self) -> None:
        node_ids = {node["node_id"] for node in self.graph["nodes"]}
        for edge in self.graph["edges"]:
            if edge["status"] == "accepted":
                self.assertIn(edge["source"], node_ids)
                self.assertIn(edge["target"], node_ids)

    def test_foundational_gpt_relation_is_accepted(self) -> None:
        accepted = {
            (edge["source"], edge["target"], edge["relation"])
            for edge in self.graph["edges"]
            if edge["status"] == "accepted"
        }
        self.assertIn(("model:gpt", "model:transformer", "es_un"), accepted)

    def test_vocabulary_is_loaded_from_yaml(self) -> None:
        vocabulary, errors = load_vocabulary()
        self.assertEqual(errors, [])
        self.assertIn("utilitza", vocabulary["relations"])
        self.assertIn("utilitzat_per", vocabulary["relations"])


if __name__ == "__main__":
    unittest.main()
