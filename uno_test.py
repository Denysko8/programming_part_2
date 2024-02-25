"""unittest module for testing function"""

import unittest
from uno_code import is_monotonic

print(unittest.__doc__)

class TestIsMonotonic(unittest.TestCase):
    """unittest class"""

    def test_is_monotonic_increasing(self):
        """checks if 'is_monotonic' function increases"""
        self.assertTrue(is_monotonic([1, 2, 3, 3, 4, 4]))

    def test_is_monotonic_decreasing(self):
        """checks if 'is_monotonic' function decreases"""
        self.assertTrue(is_monotonic([5, 5, 4, 3, 2, 2]))

    def test_is_not_monotonic(self):
        """checks if 'is_monotonic' is nor monotonic"""
        self.assertFalse(is_monotonic([1, 2, 3, 4, 3, 5]))


if __name__ == "__main__":
    unittest.main()