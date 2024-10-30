class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

# Example Usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
inorder_traversal(root)  # Output: 2 1 3
