class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# O(n) time | O(n) space
def invertBinaryTreeIterative(root):
    queue = [root]
    while len(queue):
        curentNode = queue.pop(0)
        if curentNode is None:
            continue
        swap(curentNode)
        queue.append(curentNode.left)
        queue.append(curentNode.right)

def swap(node):
    node.left, node.right = node.right, node.left

# O(n) time | O(d) space [d = depth of the tree]
def invertBinaryTreeRecursive(node):
    if node is None:
        return 
    swap(node)
    invertBinaryTreeRecursive(node.left)
    invertBinaryTreeRecursive(node.right)