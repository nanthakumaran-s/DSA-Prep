class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def findIntersection(self, l1, l2):
        if not l1 or not l2:
            return None

        a = l1
        b = l2

        while a != b:
            a = l2 if a == None else a.next
            b = l1 if b == None else b.next

        return a

if __name__ == "__main__":
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(8)
    root.next.next.next = Node(7)
    root.next.next.next.next = Node(6)


    root2 = Node(1)
    root2.next = Node(2)
    root2.next.next = Node(8)
    root2.next.next.next = Node(7)
    root2.next.next.next.next = root.next.next

    s = Solution()
    print(s.findIntersection(root, root2))