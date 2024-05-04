import unittest
from src.find_min_wire_length import read_data, minimum_spanning_tree


class TestMinimumSpanningTree(unittest.TestCase):

    def test_minimum_spanning_tree_with_connections(self):
        graph = read_data()
        total_distance = minimum_spanning_tree(graph)
        self.assertEqual(total_distance, 430)

    def test_minimum_spanning_tree_without_connections(self):
        graph = read_data()
        total_distance = minimum_spanning_tree(graph)
        self.assertEqual(total_distance, 0)


if __name__ == "__main__":
    unittest.main()
