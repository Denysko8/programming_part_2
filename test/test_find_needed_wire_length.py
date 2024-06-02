import unittest
from src.find_needed_wire_length import max_wire_length_required


class TestMaxWireLength(unittest.TestCase):
    def test_case_1(self):
        width = 2
        heights = [3, 3, 3]
        expected = 5.66
        result = max_wire_length_required(width, heights)
        self.assertAlmostEqual(result, expected, places=2)

    def test_case_2(self):
        width = 100
        heights = [1, 1, 1, 1]
        expected = 300.0
        result = max_wire_length_required(width, heights)
        self.assertAlmostEqual(result, expected, places=2)

    def test_case_3(self):
        width = 4
        heights = [100, 2, 100, 2, 100]
        expected = 396.32
        result = max_wire_length_required(width, heights)
        self.assertAlmostEqual(result, expected, places=2)

    def test_case_4(self):
        width = 4
        heights = [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28, 2, 95, 97, 60, 93, 40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72]
        expected = 2738.18
        result = max_wire_length_required(width, heights)
        self.assertAlmostEqual(result, expected, places=2)


if __name__ == '__main__':
    unittest.main()