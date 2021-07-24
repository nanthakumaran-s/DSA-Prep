class Solution: 
    # O(n) time | O(n) space
    def hashTableMethod(self, array, target):
        hashTable = {}
        for idx, val in enumerate(array):
            comp = target - val
            if comp in hashTable:
                return [comp, val]
            else:
                hashTable[val] = True
        return []

    # O(n log(n)) time | O(1) space
    def twoPointermethod(self, array, target):
        array.sort()
        left = 0
        right = len(array) - 1
        while left < right:
            newSum = array[left] + array[right]
            if newSum == target:
                return [array[left], array[right]]
            elif newSum > target:
                right -= 1
            elif newSum < target:
                left += 1
        return []

s = Solution()
array = [3, 10, 4, 9, 6, 5]
target = 19
print(s.hashTableMethod(array, target))
print(s.twoPointermethod(array, target))