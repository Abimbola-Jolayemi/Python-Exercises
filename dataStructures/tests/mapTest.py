import unittest
import map

class TestMap(unittest.TestCase):
    def setUp(self):
        self.map = map.Map()

    def test_map_size_is_zero_when_nothing_is_put_in_it(self):
        self.assertEqual(self.map.get_size(), 0)
        self.assertTrue(self.map.is_empty())

    def test_add_a_key_and_value_map_size_becomes_one(self):
        self.map.put("key", "value")
        self.assertEqual(self.map.get_size(), 1)
        self.assertFalse(self.map.is_empty())

    def test_add_a_key_and_value_map_size_becomes_two(self):
        self.map.put("key1", "value1")
        self.assertEqual(self.map.get_size(), 1)
        self.map.put("key2", "value2")
        self.assertEqual(self.map.get_size(), 2)

    def test_that_map_can_check_if_a_key_is_present(self):
        self.map.put("Key1", "value1")
        self.map.put("Key2", "value2")
        self.map.put("Key3", "value3")
        self.assertTrue(self.map.contains_key("Key2"))

    def test_that_when_two_identical_key_value_pairs_are_added_size_remains_the_same_value_is_changed(self):
        self.map.put("key1", "value1")
        self.assertEqual(self.map.get_size(), 1)
        self.map.put("key2", "value2")
        self.assertEqual(self.map.get_size(), 2)
        self.map.put("key1", "value3")
        self.assertEqual(self.map.get_size(), 2)

    def test_that_map_can_check_if_a_value_is_present(self):
        self.map.put("key1", "value1")
        self.map.put("key2", "value2")
        self.map.put("key3", "value3")
        self.assertTrue(self.map.contains_value("value2"))

    def test_that_map_can_return_value_of_a_key(self):
        self.map.put("key1", "value1")
        self.map.put("key2", "value2")
        self.map.put("key3", "value3")
        self.assertEqual(self.map.get("key3"), "value3")

    def test_that_map_cannot_return_value_of_a_key_that_is_not_present(self):
        self.map.put("key1", "value1")
        self.map.put("key2", "value2")
        self.map.put("key3", "value3")
        self.assertIsNone(self.map.get("key10"))

    def test_that_a_key_value_pair_can_be_removed_and_size_is_reduced_by_one(self):
        self.map.put("key1", "value1")
        self.map.put("key2", "value2")
        self.map.put("key3", "value3")
        self.map.put("key4", "value4")
        self.assertEqual(self.map.get_size(), 4)
        self.map.remove("key3")
        self.assertIsNone(self.map.get("key3"))

    def test_that_all_pairs_in_a_map_can_be_cleared(self):
        self.map.put("key1", "value1")
        self.map.put("key2", "value2")
        self.map.put("key3", "value3")
        self.assertEqual(self.map.get_size(), 3)
        self.map.clear()
        self.assertEqual(self.map.get_size(), 0)

    def test_that_no_item_can_be_gotten_from_the_map_after_map_has_been_cleared(self):
        self.map.put("key1", "value1")
        self.map.put("key2", "value2")
        self.map.put("key3", "value3")
        self.map.clear()
        self.assertEqual(self.map.get_size(), 0)
        self.assertIsNone(self.map.get("key1"))
        self.assertIsNone(self.map.get("key2"))
        self.assertIsNone(self.map.get("key3"))

if __name__ == '__main__':
    unittest.main()
