class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:

    def sumUsingStack(self, l1, l2):
        s1, s2, s3 = [], [], []

        while l1 or l2:
            if l1:
                s1.append(l1.value)
                l1 = l1.next
            if l2:
                s2.append(l2.value)
                l2 = l2.next

        carry = 0
        while s1 or s2 or carry:
            totalSum = 0
            if s1:
                totalSum += s1.pop()
            if s2:
                totalSum += s2.pop()
            totalSum += carry
            carry = totalSum // 10
            s3.append(totalSum % 10)

        dummy = Node(0)
        temp = dummy

        while s3:
            node = Node(s3.pop())
            temp.next = node
            temp = temp.next

        return dummy.next

    def sumOfNodesUsingReverse(self, l1, l2):
        dummy = Node(0)
        temp = dummy
        l1 = self._reverse(l1)
        l2 = self._reverse(l2)
        carry = 0

        while l1 or l2 or carry:
            totalSum = 0
            if l1:
                totalSum += l1.value
                l1 = l1.next

            if l2:
                totalSum += l2.value
                l2 = l2.next

            totalSum += carry
            carry = totalSum / 10
            node = Node(totalSum % 10)
            temp.next = node
            temp = temp.next
        
        return self._reverse(dummy.next)

    def _reverse(self, head):
        prev, cur = None, head
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev

    def printNode(self, node):
        while node:
            print(node.value)
            node = node.next

l1 = Node(5)
l1.next = Node(6)
l1.next.next = Node(3)

l2 = Node(8)
l2.next = Node(4)
l2.next.next = Node(2)

Solution().printNode(Solution().sumOfNodesUsingReverse(l1, l2))
print("----")

l1 = Node(5)
l1.next = Node(6)
l1.next.next = Node(3)

l2 = Node(8)
l2.next = Node(4)
l2.next.next = Node(2)
Solution().printNode(Solution().sumUsingStack(l1, l2))