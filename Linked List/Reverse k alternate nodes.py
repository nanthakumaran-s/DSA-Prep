class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def printLi(self, root):
        while root != None:
            print(root.value)
            root = root.next
        print("----")

    def reverse(self, root, k):
        if root is None or k == 1:
            return root

        dummy = Node(0)
        dummy.next = root

        self.printLi(dummy.next)

        cur, nex, pre = dummy, dummy, dummy
        count = 0

        while cur.next != None:
            cur = cur.next
            count += 1

        while count >= k:
            cur = pre.next
            nex = cur.next
            for i in range(k - 1):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            count -= k
        
        self.printLi(dummy.next)
        return dummy.next

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = Node(6)
root.next.next.next.next.next.next = Node(7)

Solution().reverse(root, 3)
