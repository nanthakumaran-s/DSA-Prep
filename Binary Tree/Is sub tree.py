class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def _inOrder(self, node, result):
        if node:
            self._inOrder(node.left, result)
            result.append(node.value)
            self._inOrder(node.right, result)
        return result

    def _preOrder(self, node, result):
        if node:
            result.append(node.value)
            self._preOrder(node.left, result)
            self._preOrder(node.right, result)
        return result    
    
    def check(self, s, t):
        if not t:
            return False
        elif not s and not t:
            return True    
        inT = self._inOrder(t, [])
        inS = self._inOrder(s, [])
        if not self._validate(inT, inS):
            return False
        preT = self._preOrder(t, [])
        preS = self._preOrder(s, [])
        return self._validate(preT, preS)

    def _validate(self, array1, array2):
        leftMain, leftSub = 0, 0
        while leftMain < len(array1) and leftSub < len(array2):
            if array1[leftMain] == array2[leftSub]:
                leftSub += 1
            leftMain += 1
        return leftSub == len(array2)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

s = Node(2)
s.left = Node(4)
s.right = Node(5)

print(Solution().check(s, root))