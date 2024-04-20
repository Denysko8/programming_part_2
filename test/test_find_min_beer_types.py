import unittest

from programming_part_2.src.find_min_beer_types import min_amount_of_beer_types


class TestMinAmountOfBeerTypes(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(min_amount_of_beer_types(2, 2, "YNNY"), 2)
        self.assertEqual(min_amount_of_beer_types(6, 3, "YNNYNYNYNYYNYYNYNY"), 2)
        self.assertEqual(min_amount_of_beer_types(1, 3, "YNY"), 1)

    def test_invalid_input(self):
        self.assertIsNone(min_amount_of_beer_types(0, 3, "YNNYNYNYNYYNYYNYNYYNYN"))
        self.assertIsNone(min_amount_of_beer_types(2, 5, "YNNYNYNYNYYNYYNYNYYNYN"))
        self.assertIsNone(min_amount_of_beer_types(2, 2, "NNNN"))
        self.assertIsNone(min_amount_of_beer_types(2, 2, ""))
        self.assertIsNone(min_amount_of_beer_types(2, 2, "NNNNY"))


if __name__ == '__main__':
    unittest.main()

