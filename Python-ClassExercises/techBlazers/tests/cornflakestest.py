from unittest import TestCase
from cornflakes import *

class TestCornflakes(TestCase):
    def test_that_biggest_odd_function_exist(self):
        biggest_odd("23956")

    def test_biggest_odd_number(self):
        self.assertEqual(biggest_odd("23956"), 9)

    def test_that_checks_for_equal_strings(self):
        self.assertTrue(equal_strings("love", "evol"), True)
        self.assertTrue(equal_strings("love", "wool"), False)

    def test_that_checks_for_not_equal_strings(self):
        self.assertTrue(equal_strings("love", "wool"), False)
        self.assertTrue(equal_strings("love", "evol"), True)


class TestKeyCubes(TestCase):
    def test_that_returns_a_dict_of_numbers_cube(self):
        self.assertEqual(get_key_cube([1, 2, 3, 4, 5]), {1:1, 2:8, 3:27, 4:64, 5:125})
