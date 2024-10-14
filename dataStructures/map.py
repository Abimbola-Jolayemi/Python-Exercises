class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class Map:
    def __init__(self):
        self.pair = [None] * 2
        self.size = 0

    def get_size(self):
        return self.size

    def put(self, key, value):
        if self.size == len(self.pair):
            self.resize()

        for index in range(self.size):
            if self.contains_key(key):
                self.pair[index].set_value(value)
                return

        self.pair[self.size] = KeyValuePair(key, value)
        self.size += 1

    def resize(self):
        new_pair = [None] * (2 * len(self.pair))
        for index in range(self.size):
            new_pair[index] = self.pair[index]
        self.pair = new_pair

    def is_empty(self):
        return self.size == 0

    def contains_key(self, key):
        if self.size == 0:
            return False
        for index in range(self.size):
            if self.pair[index].get_key() == key:
                return True
        return False

    def contains_value(self, value):
        if self.size == 0:
            return False
        for index in range(self.size):
            if self.pair[index].get_value() == value:
                return True
        return False

    def get(self, key):
        if self.size == 0:
            return None
        for index in range(self.size):
            if self.pair[index].get_key() == key:
                return self.pair[index].get_value()
        return None

    def remove(self, key):
        if self.size == 0:
            return
        for index in range(self.size):
            if self.pair[index].get_key() == key:
                for j in range(index, self.size - 1):
                    self.pair[j] = self.pair[j + 1]
                self.pair[self.size - 1] = None
                self.size -= 1
                return

    def clear(self):
        if self.size == 0:
            return
        for index in range(self.size):
            self.pair[index] = None
        self.size = 0
