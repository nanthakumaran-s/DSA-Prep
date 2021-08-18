class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def diameter(root):
    if root is None:
        return 0
    result = diameterUtil(root)
    return max(result) - 1


def diameterUtil(node):
    if node is None:
        return [0, 0]

    left = diameterUtil(node.left)
    right = diameterUtil(node.right)

    internalPath = max(left[1], right[1])
    if left[0] + right[0] + 1 > internalPath:
        internalPath = left[0] + right[0] + 1

    return [max(left[0], right[0]) + 1, internalPath]

root = Node(5)
root.left = Node(5)
root.right = Node(5)
root.left.left = Node(5)
root.right.right = Node(5)
print(diameter(root))