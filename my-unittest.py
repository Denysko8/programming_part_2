import unittest
from main import calculate_work_duration


class WorkDurationTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(calculate_work_duration(5, 10, [10, 20, 30, 10, 5]), 300)

    def test_second(self):
        self.assertEqual(
            calculate_work_duration(5, 10, [10, 20, 30, 10, 5, 10, 40, 20, 10, 15]), 600)

    def test_third(self):
        self.assertEqual(calculate_work_duration(5, 10, [40, 10, 20]), 400)


if __name__ == "__main__":
    unittest.main()
