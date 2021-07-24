# O(n) time | O(1) space
class Solution:
    def isMonotonicDirectionMethod(self, array):
        if len(array) <= 2:
            return True
        
        direction = array[1] - array[0]

        for i in range(2, len(array)):
            if direction == 0:
                direction = array[i] - array[i - 1]
            else:
                if self.breaksDirection(direction, array[i - 1], array[i]):
                    return False
        
        return True

    def breaksDirection(self, direction, prev, current):
        difference = current - prev
        if direction > 0:
            return difference < 0
        return difference > 0

    def isMonotonic(self, array):
        isNonIncreasing = True
        isNonDecreasing = True

        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                isNonDecreasing = False
            elif array[i] > array[i - 1]:
                isNonIncreasing = False

        return isNonIncreasing or isNonDecreasing

s = Solution()
array = [-10, -4, -2, 13, 34, 60]
print(s.isMonotonicDirectionMethod(array))
print(s.isMonotonic(array))