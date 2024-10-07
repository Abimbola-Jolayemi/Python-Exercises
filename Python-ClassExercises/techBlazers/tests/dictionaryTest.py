import unittest

from dictionary import return_dict


class MyTestCase(unittest.TestCase):
    def test_that_function_can_return_dict_of_characters(self):
        characters = "abimbolajolayemi"
        result = return_dict(characters)
        self.assertEqual(result, {'a': 3, 'b': 2, 'i': 2, 'm': 2, 'o': 2, 'l': 2, 'j': 1, 'y': 1, 'e': 1})

    def test_that_function_can_return_dict_of_characters_ignoring_case(self):
        characters = "AbimbolaJolayemi"
        result = return_dict(characters)
        self.assertEqual(result, {'a': 3, 'b': 2, 'i': 2, 'm': 2, 'o': 2, 'l': 2, 'j': 1, 'y': 1, 'e': 1})

    def test_that_function_cannot_return_dict_of_unstringed_numbers(self):
        with self.assertRaises(TypeError):
            return_dict(1)

if __name__ == '__main__':
    unittest.main()
