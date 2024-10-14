import unittest
import linkedList

class TestLinkedList(unittest.TestCase):

    def test_that_linked_list_is_empty(self):
        linked_list = linkedList.LinkedList()
        self.assertTrue(linked_list.is_empty())

    def test_that_a_new_node_can_be_added_to_the_linked_list_list_is_not_empty(self):
        linked_list = linkedList.LinkedList()
        linked_list.add("Item 1")
        linked_list.add("Item 2")
        self.assertFalse(linked_list.is_empty())

    def test_that_when_a_new_node_is_added_size_is_increased(self):
        linked_list = linkedList.LinkedList()
        linked_list.add("Item 1")
        linked_list.add("Item 2")
        linked_list.add("Item 3")
        linked_list.add("Item 4")
        self.assertFalse(linked_list.is_empty())
        self.assertEqual(linked_list.get_size(), 4)

    def test_that_linked_list_can_be_emptied(self):
        linked_list = linkedList.LinkedList()
        linked_list.add("Item 1")
        linked_list.add("Item 2")
        linked_list.add("Item 3")
        linked_list.add("Item 4")
        self.assertFalse(linked_list.is_empty())
        linked_list.clear()
        self.assertTrue(linked_list.is_empty())

    def test_that_if_list_is_emptied_size_returns_to_zero(self):
        linked_list = linkedList.LinkedList()
        linked_list.add("Item 1")
        linked_list.add("Item 2")
        linked_list.add("Item 3")
        linked_list.add("Item 4")
        linked_list.clear()
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.get_size(), 0)

    def test_that_an_element_can_be_removed_by_index(self):
        linked_list = linkedList.LinkedList()
        linked_list.add("Item 1")
        linked_list.add("Item 2")
        linked_list.add("Item 3")
        linked_list.add("Item 4")
        linked_list.remove_at(2)
        self.assertFalse(linked_list.is_empty())
        self.assertEqual(linked_list.get_size(), 3)

    def test_that_linked_cannot_remove_an_item_beyond_the_present_list_size(self):
        linked_list = linkedList.LinkedList()
        linked_list.add("Item 1")
        linked_list.add("Item 2")
        linked_list.add("Item 3")
        linked_list.add("Item 4")
        with self.assertRaises(IndexError):
            linked_list.remove_at(7)

    def test_that_linked_can_remove_item_by_node_element(self):
        linked_list = linkedList.LinkedList()
        linked_list.add("Item 1")
        linked_list.add("Item 2")
        linked_list.add("Item 3")
        linked_list.add("Item 4")
        linked_list.remove("Item 3")
        self.assertFalse(linked_list.is_empty())
        self.assertEqual(linked_list.get_size(), 3)

if __name__ == "__main__":
    unittest.main()
