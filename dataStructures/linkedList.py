class Node:
    def __init__(self, element):
        self.element = element
        self.next_node = None

    def get_element(self):
        return self.element

    def get_next_node(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.capacity = 2
        self.node_array = [None] * self.capacity  # Store node references

    def get_size(self):
        return self.size

    def add(self, element):
        if self.size == self.capacity:
            self.reset_capacity()
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.node_array[self.size] = new_node
        self.size += 1

    def reset_capacity(self):
        new_node_array = [None] * (self.capacity * 2)
        for index in range(len(self.node_array)):
            new_node_array[index] = self.node_array[index]
        self.node_array = new_node_array
        self.capacity *= 2

    def remove_at(self, index_of_item):
        if index_of_item < 0 or index_of_item >= self.size:
            raise IndexError(f"Index {index_of_item} is out of bounds")

        node_to_remove = self.node_array[index_of_item]
        if index_of_item == 0:
            self.head = self.head.get_next_node()
            if self.head is None:
                self.tail = None
        else:
            previous_node = self.node_array[index_of_item - 1]
            previous_node.set_next(node_to_remove.get_next_node())
            if node_to_remove == self.tail:
                self.tail = previous_node

        for index in range(index_of_item, self.size - 1):
            self.node_array[index] = self.node_array[index + 1]
        self.node_array[self.size - 1] = None  # Clear the last reference
        self.size -= 1

    def remove(self, element):
        if self.head is None:
            return False

        if self.head.get_element() == element:
            self.head = self.head.get_next_node()
            self.size -= 1
            return True

        current_node = self.head
        while current_node.get_next_node() is not None:
            if current_node.get_next_node().get_element() == element:
                current_node.set_next(current_node.get_next_node().get_next_node())
                self.size -= 1
                return True
            current_node = current_node.get_next_node()
        return False

    def is_empty(self):
        return self.size == 0

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current_node = self.head
        while current_node is not None:
            print(f"{current_node.get_element()} -> ", end="")
            current_node = current_node.get_next_node()
        print("null")

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
