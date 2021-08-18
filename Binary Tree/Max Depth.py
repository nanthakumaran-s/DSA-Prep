class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time | O(n) space
def depth(node):
    if node is None:
        return 0
    
    left = depth(node.left)
    right = depth(node.right)
    return max(left, right) + 1

root = BinaryTree(5)
root.left = BinaryTree(5)
root.right = BinaryTree(5)
root.left.left = BinaryTree(5)
root.right.right = BinaryTree(5)
print(depth(root))
            