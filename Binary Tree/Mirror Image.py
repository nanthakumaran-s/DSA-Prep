class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def mirror(self, a, b):
        if a is None and b is None:
            return True

        if a is None or b is None:
            return False

        return a.value == b.value and self.mirror(a.left, b.right) and self.mirror(a.right, b.left)

root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root2.left = Node(3)
root2.right = Node(2)
root2.right.left = Node(5)
root2.right.right = Node(4)

print(Solution().mirror(root1, root2))