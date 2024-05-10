import unittest

from src.find_needed_wire_length import find_needed_wire_length


class TestFindNeededWireLength(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(find_needed_wire_length(2, [3, 1, 3]), 5.66)

    def test_invalid_input(self):
        self.assertIsNone(find_needed_wire_length(0, [3, 1, 3]))
        self.assertIsNone(find_needed_wire_length(2, [0, 1, 3]))
