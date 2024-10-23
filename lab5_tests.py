import data
import lab5
import unittest
from lab5 import time_add, is_descending
from data import Time


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add_1(self):
        tester = time_add(Time(4, 2, 1), Time(6, 12, 3))
        self.assertEqual(tester, Time(10, 14, 4))

    def test_time_add_2(self):
        tester = time_add(Time(4,50,15), Time(1,9, 106))
        self.assertEqual(tester, Time(6,1, 1))

    # Part 4
    def test_is_descending_1(self):
        test_list = [4.1, 3.9, 2.765, 1.0]
        self.assertEqual(is_descending(test_list), True)

    def test_is_descending_2(self):
        test_list = [4.1, 7.2, 2.765, 1.0]
        self.assertEqual(is_descending(test_list), False)
    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
