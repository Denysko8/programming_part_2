import unittest

from src.needle_in_haystack import find_needle_in_haystack


class TestPriorityQueue(unittest.TestCase):

    def test_single_index(self):
        self.assertEqual(find_needle_in_haystack("abcab", "abcab"), "0")

    def test_double_index(self):
        self.assertEqual(find_needle_in_haystack("ababcababcabcabc", "abcabc"), "7,10")

    def test_no_index(self):
        self.assertEqual(find_needle_in_haystack("ababcab", "abcabd"), None)


if __name__ == "__main__":
    unittest.main()
