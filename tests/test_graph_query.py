"""Proves unitàries del motor GraphQA determinista."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from graph_query import GraphQuery, QueryError  # noqa: E402


SAMPLE_GRAPH = {
    "nodes": [
        {"node_id": "model:g_retriever", "title": "G-Retriever", "path": "models/G-Retriever.md"},
        {"node_id": "concept:graphqa", "title": "GraphQA", "path": "conceptes/GraphQA.md"},
        {"node_id": "concept:graphrag", "title": "GraphRAG", "path": "conceptes/GraphRAG.md"},
        {"node_id": "concept:rag", "title": "RAG", "path": "conceptes/RAG.md"},
    ],
    "edges": [
        {"source": "model:g_retriever", "target": "concept:graphqa", "relation": "aplicat_a", "status": "accepted", "claim_type": "documented", "confidence": "high", "evidence": ["paper"]},
        {"source": "model:g_retriever", "target": "concept:graphrag", "relation": "utilitza", "status": "accepted", "claim_type": "documented", "confidence": "medium", "evidence": ["fitxa"]},
        {"source": "concept:graphrag", "target": "concept:rag", "relation": "amplia", "status": "accepted", "claim_type": "documented", "confidence": "high", "evidence": ["docs"]},
        {"source": "concept:graphqa", "target": "concept:rag", "relation": "wikilink", "status": "candidate", "claim_type": "structural", "confidence": "low"},
    ],
}


class GraphQueryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.query = GraphQuery(SAMPLE_GRAPH)

    def test_resolve_accepts_id_title_and_path(self) -> None:
        expected = "concept:graphrag"
        self.assertEqual(self.query.resolve(expected), expected)
        self.assertEqual(self.query.resolve("graphrag"), expected)
        self.assertEqual(self.query.resolve("conceptes/GraphRAG.md"), expected)

    def test_neighbours_include_both_directions(self) -> None:
        result = self.query.neighbours("GraphRAG")
        self.assertEqual({item["direction"] for item in result}, {"incoming", "outgoing"})

    def test_path_finds_shortest_directed_route(self) -> None:
        result = self.query.path("G-Retriever", "RAG", max_depth=2)
        self.assertIsNotNone(result)
        self.assertEqual(
            [node["node_id"] for node in result["nodes"]],
            ["model:g_retriever", "concept:graphrag", "concept:rag"],
        )

    def test_path_respects_max_depth(self) -> None:
        self.assertIsNone(self.query.path("G-Retriever", "RAG", max_depth=1))

    def test_subgraph_uses_undirected_neighbourhood(self) -> None:
        result = self.query.subgraph("GraphRAG", depth=1)
        self.assertEqual(
            {node["node_id"] for node in result["nodes"]},
            {"model:g_retriever", "concept:graphrag", "concept:rag"},
        )

    def test_explain_edge_returns_provenance(self) -> None:
        result = self.query.explain_edge("GraphRAG", "RAG")
        self.assertEqual(result[0]["edge"]["evidence"], ["docs"])
        self.assertEqual(result[0]["direction"], "forward")

    def test_candidates_are_excluded_by_default(self) -> None:
        self.assertEqual(self.query.explain_edge("GraphQA", "RAG"), [])
        with_candidates = GraphQuery(SAMPLE_GRAPH, include_candidates=True)
        self.assertEqual(len(with_candidates.explain_edge("GraphQA", "RAG")), 1)

    def test_unknown_node_is_an_error(self) -> None:
        with self.assertRaises(QueryError):
            self.query.resolve("inexistent")


if __name__ == "__main__":
    unittest.main()
