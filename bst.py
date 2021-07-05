class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, current, value):
        if self.root is None:
            self.root = Node(value)
        else:
            if current.value < value:
                if current.left is None:
                    current.left = Node(value)
                else:
                    self.insert(current.left, value)
            else:
                if current.right is None:
                    current.right = value
                else:
                    self.insert(current.right, value)

    def visit(self, node):
        print(node.value)

    def preorder(self, current):
        """
        1. visit
        2. go left
        3. go right
        """
        self.visit(current)
        self.preorder(current.left)
        self.preorder(current.right)

    def inorder(self, current):
        """
        1. go left
        2. visit
        3. go right
        """
        self.inorder(current.left)
        self.visit(current)
        self.inorder(current.right)

    def postorder(self, current):
        """
        1. go left
        2. go right
        3. visit
        """
        self.postorder(current.left)
        self.postorder(current.right)
        self.visit(current)

    def search(self, current, key):
        if current is None or current.value == key:
            return current

        if current.value < key:
            self.search(current.right, key)

        self.search(current.left, key)
