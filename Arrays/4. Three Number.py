class Solution:
    # O(n^2) time | O(n) space
    def threeNumber(self, array, target):
        array.sort()
        triplets = []
        for i in range(len(array) - 2):
            left = i + 1
            right = len(array) - 1
            while left < right:
                newSum = array[i] + array[left] + array[right]
                if newSum == target:
                    triplets.append([array[i], array[left], array[right]])
                    left += 1
                    right -= 1
                elif newSum > target:
                    right -= 1
                elif newSum < target:
                    left += 1
        return triplets


s = Solution()
array = [1, 10, 3, 15, 2, 9, 5, 2]
target = 9
print(s.threeNumber(array, target))
