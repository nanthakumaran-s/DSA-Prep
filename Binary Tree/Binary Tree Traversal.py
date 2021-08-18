class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Traversal:
    def inOrder(self, root, inOrderArray):
        if root:
            self.inOrder(root.left, inOrderArray)
            inOrderArray.append(root.value)
            self.inOrder(root.right, inOrderArray)
        return inOrderArray

    def postOrder(self, root, postOrderArray):
        if root:
            self.postOrder(root.left, postOrderArray)
            self.postOrder(root.right, postOrderArray)
            postOrderArray.append(root.value)
        return postOrderArray

    def preOrder(self, root, preOrderArray):
        if root:
            preOrderArray.append(root.value)
            self.preOrder(root.left, preOrderArray)
            self.preOrder(root.right, preOrderArray)
        return preOrderArray

    def preOrderOnlyUsingRight(self, root):
        stack = [root]
        pre = None
        while stack:
            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            if pre:
                pre.right = node
            pre = node
        return pre

    def levelOrder(self, root):
        if root is None:
            return []
        q = [root]
        levelOrderArray = []
        while len(q):
            node = q.pop(0)
            levelOrderArray.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return levelOrderArray

    def spiralTraversal(self, root):
        results = []
        q = [root]
        while q:
            currentLvl = []
            for i in range(len(q)):
                node = q.pop(0)
                currentLvl.append(node.value)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            results.append(currentLvl)
        for i in range(len(results)):
            if i % 2 != 0:
                col = 0
                endCol = len(results[i]) - 1
                while col < endCol:
                    results[i][col], results[i][endCol] = results[i][endCol], results[i][col]
                    col += 1
                    endCol -= 1
        return results

    def spiralTraversalWithoutLevelVaraible(self, root):
        s1 = [] # right to left
        s2 = [] # left to right
        s2 = [root]
        results = []
        while s1 or s2:
            while s1:
                node = s1.pop()
                results.append(node.value)
                if node.right:
                    s2.append(node.right)
                if node.left:
                    s2.append(node.left)
            while s2:
                node = s2.pop()
                results.append(node.value)
                if node.left:
                    s1.append(node.left)
                if node.right:
                    s1.append(node.right)
        return results

    def treeToString(self, node, string): # parenthesization
        if node is None:
            return
        string.append(str(node.value))
        if node.left:
            string.append("(")
            self.treeToString(node.left, string)
            string.append(")")
        if node.right:
            string.append("(")
            self.treeToString(node.right, string)
            string.append(")")

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    traversal = Traversal()
    print(traversal.inOrder(root, []))
    print(traversal.postOrder(root, []))
    print(traversal.preOrder(root, []))
    print(traversal.levelOrder(root))
    print(traversal.spiralTraversal(root))
    print(traversal.spiralTraversalWithoutLevelVaraible(root))

    string = []
    traversal.treeToString(root, string)
    print("".join(string))