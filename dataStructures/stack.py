from logging import NullHandler


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack_list = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def push(self, item):
        if not self.is_full():
            self.stack_list.append(item)
            self.size += 1
            is_empty = False

    def pop(self):
        if self.is_empty():
            return None
        item = self.stack_list[self.size - 1]
        self.size -= 1
        return item

    def is_full(self):
        return self.size == self.capacity

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[self.size - 1]

    def contains(self, item_to_check):
        if self.is_empty():
            return False
        for item in self.stack_list:
            if item == item_to_check:
                return True
        return False

    def search(self, item_to_search):
        if self.is_empty():
            return None
        for item in self.stack_list:
            if item == item_to_search:
                return self.stack_list.index(item)
        return None

    def clear(self):
        self.stack_list = []
        self.size = 0
