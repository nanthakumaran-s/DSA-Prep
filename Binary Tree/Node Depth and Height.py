class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepth(node, x):
    if node is None:
        return -1
    
    dist = - 1
    if node.value == x:
        return dist + 1

    dist = nodeDepth(node.left, x)
    if dist >= 0:
        return dist + 1
    dist = nodeDepth(node.right, x)
    if dist >= 0:
        return dist + 1
    
    return dist

def nodeHeight(node, x):
    global height
    heighthelper(node, x)
    return height

def heighthelper(node, x):
    global height
    if node is None:
        return -1
    
    leftheight = heighthelper(node.left, x)
    rightheight = heighthelper(node.right, x)

    ans = max(leftheight, rightheight) + 1
    if node.value == x:
        height = ans

    return ans

height = -1
root = Node(5)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(20)
root.left.right = Node(25)
root.left.right.right = Node(45)
root.right.left = Node(30)
root.right.right = Node(35)

print(nodeDepth(root, 25))
print(nodeHeight(root, 25))