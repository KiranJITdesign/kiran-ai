"""Unit tests for the KiranNano Search and Retrieval Augmentation Engine."""

import unittest
from kiran_ai.memory.hierarchy import HierarchicalMemoryManager, SemanticFact
from kiran_ai.search.engine import SearchEngine, SearchResult


class TestSearchEngine(unittest.TestCase):
    def setUp(self):
        self.mem = HierarchicalMemoryManager(session_id="test_search_session")
        self.mem.semantic.insert_fact(
            SemanticFact(
                fact_id="fact-1",
                subject="KiranNano",
                predicate="is an",
                object_value="ultra-compact neural model engineered by S Kiran",
                confidence=1.0,
            )
        )
        self.engine = SearchEngine(memory_manager=self.mem, timeout=1.0)

    def test_offline_semantic_memory_search(self):
        # When network is unreachable or in sandbox, search falls back to semantic memory
        from unittest.mock import patch
        with patch("urllib.request.urlopen", side_effect=OSError("Network offline")):
            results = self.engine.search("KiranNano")
            self.assertIsInstance(results, list)
            self.assertGreater(len(results), 0)
            self.assertIn("KiranNano", results[0].title)

    def test_search_and_summarize(self):
        summary = self.engine.search_and_summarize("KiranNano")
        self.assertIsInstance(summary, str)
        self.assertIn("Search & Research Summary", summary)
        self.assertIn("KiranNano", summary)

    def test_search_unknown_fallback(self):
        summary = self.engine.search_and_summarize("NonExistentTermXYZ1234")
        self.assertIsInstance(summary, str)
        self.assertIn("Search & Research", summary)


if __name__ == "__main__":
    unittest.main()

