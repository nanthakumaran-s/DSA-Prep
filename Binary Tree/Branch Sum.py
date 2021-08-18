class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time | O(n) space
def branchSum(self, root):
    sums = []
    self._calculate(root, 0, sums)
    return sums

def _calculate(self, node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    self._calculate(node.left, newRunningSum, sums)
    self._calculate(node.right, newRunningSum, sums)