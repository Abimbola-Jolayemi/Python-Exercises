import unittest
import set

class TestSet(unittest.TestCase):
    def setUp(self):
        self.set = set.Set(4)

    def test_set_is_empty_when_no_item_is_added(self):
        self.assertEqual(self.set.get_size(), 0)

    def test_set_has_size_of_one_when_item_is_added(self):
        self.set.add(2)
        self.assertEqual(self.set.get_size(), 1)

    def test_check_if_set_contains_an_item(self):
        self.set.add(1)
        self.set.add(2)
        self.set.add(3)
        self.set.add(4)
        self.assertEqual(self.set.get_size(), 4)
        self.assertTrue(self.set.contains(3))

    def test_empty_set_does_not_contain_an_item(self):
        self.assertFalse(self.set.contains("1"))

    def test_set_cannot_add_number_present_in_set(self):
        self.set.add(2)
        self.set.add(3)
        self.assertEqual(self.set.get_size(), 2)
        self.set.add(2)
        self.assertEqual(self.set.get_size(), 2)

    def test_set_cannot_add_number_when_full(self):
        self.set.add("item 1")
        self.set.add("item 2")
        self.set.add("item 3")
        self.set.add("item 4")
        self.assertEqual(self.set.get_size(), 4)
        self.set.add("item 5")
        self.assertEqual(self.set.get_size(), 4)

    def test_set_can_be_cleared(self):
        self.set.add("item 1")
        self.set.add("item 2")
        self.set.add("item 3")
        self.set.add("item 4")
        self.assertEqual(self.set.get_size(), 4)
        self.set.clear()
        self.assertEqual(self.set.get_size(), 0)

    def test_set_can_return_array_of_its_elements(self):
        self.set.add("item 1")
        self.set.add("item 2")
        self.set.add("item 3")
        self.set.add("item 4")
        self.assertEqual(self.set.get_size(), 4)
        expected_array = ["item 1", "item 2", "item 3", "item 4"]
        self.assertListEqual(expected_array, self.set.to_array())

if __name__ == '__main__':
    unittest.main()
