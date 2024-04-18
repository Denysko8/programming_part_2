import unittest

from is_monotonic import is_monotonic


class TestIsMonotonic(unittest.TestCase):

    def test_is_monotonic_increasing(self):
        self.assertTrue(is_monotonic([1, 2, 3, 3, 4, 4]))

    def test_is_monotonic_decreasing(self):
        self.assertTrue(is_monotonic([5, 5, 4, 3, 2, 2]))

    def test_is_not_monotonic(self):
        self.assertFalse(is_monotonic([1, 2, 3, 4, 3, 5]))


if __name__ == '__main__':
    unittest.main()
