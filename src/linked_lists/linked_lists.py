class LinkedListNode:
    def __init__(self, next_node, value):
        self.next_node = next_node
        self.value = value

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(next_node={self.next_node}, value={self.value})"
        )

    def __str__(self):
        return str(self.value)


class LinkedList:
    head = None

    def __repr__(self):
        return f"{self.__class__.__name__}(head={self.head})"

    def __str__(self):
        return str(self.head)

    def add(self, value):
        self.head = LinkedListNode(self.head, value)

    def append(self, value):
        last_node = self.head
        try:
            while last_node.next_node is not None:
                last_node = last_node.next_node
        except AttributeError:
            self.head = LinkedListNode(None, value)
        else:
            last_node.next_node = LinkedListNode(None, value)

    def remove_first(self):
        self.head = self.head.next_node

    def remove_last(self):
        second_last_node = self.head
        last_node = self.head.next_node
        try:
            while last_node.next_node is not None:
                second_last_node = last_node
                last_node = last_node.next_node
        except AttributeError:
            self.head = None
            return

        second_last_node.next_node = None

    def print(self):
        temporary_node = self.head
        while temporary_node:
            print(temporary_node.value, end="-")
            temporary_node = temporary_node.next_node
