class Queue:
    def __init__(self, capacity):
        self.current_size = 0
        self.capacity = capacity
        self.queueList = []
        self.firstItem = 0

    def is_empty(self):
        return self.current_size == 0

    def enqueue(self, item):
        if self.current_size < self.capacity:
            self.queueList.append(item)
            self.current_size += 1

    def get_size(self):
        return self.current_size

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.queueList[self.firstItem]
            self.firstItem += 1
            self.current_size -= 1
            return dequeued_item
        return None
