class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and link to the next node in the list.
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"


class LinkedList:
    """
    An object for storing linked list
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds element to the head of the list
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Searches first node that matches the key.
        Return the node if key matches or None if does not match.
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts data at given index
        """
        if index == 0:
            self.add(data)
        else:
            position = 0
            current = self.head
            while position < index-1:
                current = current.next_node
                position += 1

            new_node = Node(data)
            new_node.next_node = current.next_node
            current.next_node = new_node

    def remove(self, key):
        """
        Removes element that match the key.
        """
        current = self.head
        prev = None

        while current:
            if current.data == key:
                if current is self.head:
                    self.head = current.next_node
                else:
                    prev.next_node = current.next_node
                break
            else:
                prev = current
                current = current.next_node

    def node_at_index(self, index):
        position = 0
        current = self.head

        while position < index:
            current = current.next_node
            position += 1

        return current

    def __repr__(self):
        """
        Returns list of elements of linked list
        """
        current = self.head
        nodes = []

        while current:
            nodes.append(current.data)
            current = current.next_node

        return '->'.join(map(str, nodes))


l = LinkedList()

for i in range(0, 20, 3):
    l.add(i)

