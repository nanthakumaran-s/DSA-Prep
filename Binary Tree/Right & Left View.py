class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def leftView(root):
    q = [root]
    leftView = []
    while len(q):
        for i in range(0, len(q)):
            temp = q[0]
            q.pop(0)
            if i == 0:
                leftView.append(temp.value)
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)

    return leftView

def rightView(root):
    q = [root]
    rightView = []
    while len(q):
        n = len(q)
        while n > 0:
            n -= 1
            temp = q.pop(0)
            if n == 0:
                rightView.append(temp.value)

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

    return rightView

if __name__ == '__main__':
 
    root = Node(10)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(8)
    root.right.right = Node(15)
    root.right.left = Node(12)
    root.right.right.left = Node(14)
    print(leftView(root))
    print(rightView(root))