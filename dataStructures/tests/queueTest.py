import unittest
from queue import Queue


class MyTestCase(unittest.TestCase):
    def test_that_queue_exists(self):
        queue = Queue(4)

    def test_that_queue_is_empty(self):
        queue = Queue(4)
        self.assertTrue(queue.is_empty)

    def test_that_queue_is_not_empty_queue_can_enqueue_items(self):
        queue = Queue(4)
        queue.enqueue("Item 1")
        queue.enqueue("Item 2")
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.get_size(), 2)

    def test_that_queue_can_return_size(self):
        queue = Queue(4)
        self.assertEqual(queue.get_size(), 0)
        self.assertTrue(queue.is_empty())
        queue.enqueue("Item 1")
        self.assertEqual(queue.get_size(), 1)
        self.assertFalse(queue.is_empty())
        queue.enqueue("Item 2")
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.get_size(), 2)

    def test_that_queue_cannot_enqueue_at_full_capacity(self):
        queue = Queue(4)
        self.assertEqual(queue.get_size(), 0)
        self.assertTrue(queue.is_empty())
        queue.enqueue("Item 1")
        queue.enqueue("Item 2")
        queue.enqueue("Item 3")
        queue.enqueue("Item 4")
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.get_size(), 4)
        queue.enqueue("Item 5")
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.get_size(), 4)

    def test_that_queue_can_dequeue_items_size_is_reduced_by_one(self):
        queue = Queue(4)
        queue.enqueue("Item 1")
        queue.enqueue("Item 2")
        queue.enqueue("Item 3")
        queue.enqueue("Item 4")
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.get_size(), 4)
        self.assertEqual("Item 1", queue.dequeue())
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.get_size(), 3)
        self.assertEqual("Item 2", queue.dequeue())
        self.assertEqual("Item 3", queue.dequeue())
        self.assertEqual("Item 4", queue.dequeue())
        self.assertTrue(queue.is_empty())


if __name__ == '__main__':
    unittest.main()
