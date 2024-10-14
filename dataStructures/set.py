class Set:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.list = [None] * capacity

    def get_size(self):
        return self.size

    def add(self, element):
        if not self.contains(element) and not self.is_full():
            self.list[self.size] = element
            self.size += 1

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def contains(self, element):
        if self.size == 0:
            return False
        for item in range(self.size):
            if self.list[item] == element:
                return True
        return False

    def clear(self):
        for index in range(self.size):
            self.list[index] = None
        self.size = 0

    def to_array(self):
        return [self.list[index] for index in range(self.size)]
