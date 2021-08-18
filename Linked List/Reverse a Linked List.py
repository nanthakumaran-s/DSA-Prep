class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        prev, cur = None, head
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev

    def reverseRecursive(self, head):
        if head is None or head.next is None:
            return head

        prev, cur = None, head
        self._recursiveHelper(prev, cur)
        return prev
    
    def _recursiveHelper(self, prev, cur):
        if cur is None:
            return      
        nex = cur.next
        cur.next = prev
        prev = cur
        cur = nex

    def printNodes(self, head):
        while head:
            print(head.value)
            head = head.next

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = Node(6)
root.next.next.next.next.next.next = Node(7)

Solution().printNodes(Solution().reverse(root))
print("---")
Solution().printNodes(Solution().reverse(root))