import unittest


from main import final_result, check_forward, check_backwards


class WorkDurationTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(final_result(3, 10, [50, 20, 20, 20, 20, 20, 35]), 700)

    def test_second(self):
        self.assertEqual(final_result(3, 10, [100, 20, 20, 20, 20, 20]), 1000)

    def test_third(self):
        self.assertEqual(final_result(2, 10, [100, 110, 80, 90, 120, 100]), 3100)


if __name__ == "__main__":
    unittest.main()
