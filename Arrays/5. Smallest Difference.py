class Solution:
    # O(n) time | O(1) space
    def smallestDifference(self, array1, array2):
        smallestpair = []
        smallest = float("inf")
        ptr1, ptr2 = 0, 0
        while ptr1 < len(array1) and ptr2 < len(array2):
            current = 0
            firstNum = array1[ptr1]
            secondNum = array2[ptr2]
            if firstNum == secondNum:
                return [firstNum, secondNum]
            elif firstNum > secondNum:
                current = firstNum - secondNum
                ptr2 += 1
            elif firstNum < secondNum:
                current = secondNum - firstNum
                ptr1 += 1
            
            if current < smallest:
                smallest = current
                smallestpair = [firstNum, secondNum]
        return smallestpair

s = Solution()
array1 = [1, 14, 17, 20, 34]
array2 = [4, 12, 134, 150]
print(s.smallestDifference(array1, array2))