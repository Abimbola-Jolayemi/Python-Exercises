import unittest
from stack import Stack

class MyTestCase(unittest.TestCase):
    def test_that_stack_is_empty(self):
        stack = Stack(4)
        self.assertTrue(stack.is_empty())

    def test_that_stack_can_push_items(self):
        stack = Stack(4)
        stack.push("Item 1")
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.get_size(), 1)
        stack.push("Item 2")
        self.assertTrue(not stack.is_empty())
        self.assertEqual(stack.get_size(), 2)

    def test_that_stack_has_a_capacity(self):
        stack = Stack(4)
        stack.push("Item 1")
        stack.push("Item 2")
        stack.push("Item 3")
        stack.push("Item 4")
        self.assertEqual(stack.get_size(), 4)
        self.assertTrue(stack.is_full())

    def test_a_filled_stack_cannot_add_items(self):
        stack = Stack(4)
        stack.push("Item 1")
        stack.push("Item 2")
        stack.push("Item 3")
        stack.push("Item 4")
        self.assertTrue(stack.is_full())
        stack.push("Item 5")
        self.assertEqual(stack.get_size(), 4)

    def test_that_stack_can_remove_items(self):
        stack = Stack(4)
        stack.push("Item 1")
        stack.push("Item 2")
        stack.push("Item 3")
        stack.push("Item 4")
        self.assertEqual(stack.get_size(), 4)
        self.assertEqual(stack.pop(), "Item 4")
        self.assertEqual(stack.get_size(), 3)
        self.assertEqual(stack.pop(), "Item 3")
        self.assertEqual(stack.get_size(), 2)
        self.assertEqual(stack.pop(), "Item 2")
        self.assertEqual(stack.get_size(), 1)
        self.assertEqual(stack.pop(), "Item 1")
        self.assertEqual(stack.get_size(), 0)

    def test_that_stack_can_remove_items_from_empty_stack(self):
        stack = Stack(4)
        self.assertEqual(stack.pop(), None)

    def test_that_stack_can_peek_items(self):
        stack = Stack(4)
        stack.push("Item 1")
        stack.push("Item 2")
        stack.push("Item 3")
        self.assertEqual(stack.get_size(), 3)
        self.assertEqual(stack.peek(), "Item 3")
        self.assertEqual(stack.get_size(), 3)
        
    def test_that_stack_cannot_peek_from_an_empty_stack(self):
        stack = Stack(4)
        self.assertEqual(stack.peek(), None)

    def test_if_a_stack_contains_an_item(self):
        stack = Stack(4)
        stack.push("Item 1")
        stack.push("Item 2")
        stack.push("Item 3")
        self.assertEqual(stack.get_size(), 3)
        self.assertEqual(stack.contains("Item 2"), True)
        self.assertEqual(stack.contains("Item 10"), False)

    def test_that_an_empty_stack_does_not_contain_an_item(self):
        stack = Stack(4)
        self.assertEqual(stack.get_size(), 0)
        self.assertEqual(stack.contains("Item 1"), False)

    def test_that_search_for_the_position_of_an_existing_item_in_the_stack(self):
        stack = Stack(4)
        stack.push("Item 1")
        stack.push("Item 2")
        stack.push("Item 3")
        stack.push("Item 4")
        self.assertEqual(stack.get_size(), 4)
        self.assertEqual(stack.search("Item 2"), 1)
        self.assertEqual(stack.search("Item 3"), 2)
        self.assertEqual(stack.search("Item 10"), None)

    def test_that_an_empty_stack_cannot_have_the_position_of_any_item(self):
        stack = Stack(4)
        self.assertEqual(stack.get_size(), 0)
        self.assertEqual(stack.search("Item 1"), None)

    def test_that_stack_can_clear_items_and_size_of_stack_becomes_zero(self):
        stack = Stack(4)
        stack.push("Item 1")
        stack.push("Item 2")
        stack.push("Item 3")
        stack.push("Item 4")
        self.assertEqual(stack.get_size(), 4)
        stack.clear()
        self.assertEqual(stack.get_size(), 0)






if __name__ == '__main__':
    unittest.main()