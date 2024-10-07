import unittest

from switchString import *


class MyTestCase(unittest.TestCase):
    def test_that_function_can_interchange_characters_in_a_string(self):
        my_string1 = 'abc'
        my_string2 = 'xyz'
        result = switch_string(my_string1, my_string2)
        self.assertEqual(result, 'xyc abz')

    def test_that_function_can_add_ce_to_the_end_or_middle(self):
        word1 = 'helloo'
        result = add_ce(word1)
        self.assertEqual(result, 'helceloo')

    def test_that_function_can_select_uppercase_before_lowercase(self):
        word = 'sEmICoLOn'
        result = arrange_case(word)
        self.assertEqual(result, 'EICLOsmon')
        result2 = arrange_case('semicolon')
        self.assertEqual(result2, 'semicolon')

    def test_that_function_can_return_a_tuple_of_character_occurences(self):
        self.assertEqual(get_character_occurence('semicolon', 'o'), ('o', 2))
        self.assertEqual(get_character_occurence('semicolon', 'e'), ('e', 1))

    def test_that_function_can_remove_puctuation_from_a_string(self):
        self.assertEqual(remove_punctuation('he,ll.o'), 'hello')
        self.assertEqual(remove_punctuation('@Ab.imbola12'), 'Abimbola')
if __name__ == '__main__':
    unittest.main()
