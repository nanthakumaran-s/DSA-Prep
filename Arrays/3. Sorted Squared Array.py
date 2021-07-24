class Solution:
    # O(n) time | O(n) space 
    def sortSquaredArray(self, array):
        result = [0] * len(array)
        count = len(array) - 1
        left = 0
        right = len(array) - 1
        while left < right:
            if abs(array[left]) > abs(array[right]):
                result[count] = array[left] ** 2
                left += 1
            elif abs(array[left]) < abs(array[right]):
                result[count] = array[right] ** 2
                right -= 1
            count -= 1
        return result

s = Solution()
array = [-10, -5, 0, 2, 14]
print(s.sortSquaredArray(array))