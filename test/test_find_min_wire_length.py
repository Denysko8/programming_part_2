import unittest
from programming_part_2.src.find_min_wire_length import read_data, minimum_spanning_tree


class TestMinimumSpanningTree(unittest.TestCase):

    def test_minimum_spanning_tree(self):
        file_path = "../materials/communication_wells.csv"
        graph = read_data(file_path)
        total_distance = minimum_spanning_tree(graph)
        self.assertEqual(total_distance, 430)

    def test_minimum_spanning_tree_no_connections(self):
        file_path = "../materials/communication_no_wells.csv"
        graph = read_data(file_path)
        total_distance = minimum_spanning_tree(graph)
        self.assertEqual(total_distance, -1)


if __name__ == "__main__":
    unittest.main()