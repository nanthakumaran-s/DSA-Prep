class Solution:
    # O(log(n)) time | O(log(n)) space
    def recursive(self, array, target):
        return self._recursiveHelper(array, target, 0, len(array) - 1)

    def _recursiveHelper(self, array, target, left, right):
        if left > right:
            return -1

        mid = (left + right) // 2
        potentialmatch = array[mid]
        leftNum = array[left]
        rightNum = array[right]

        if potentialmatch == target:
            return mid
        elif leftNum <= potentialmatch:
            if target < potentialmatch and target >= leftNum:
                return self._recursiveHelper(array, target, left, mid - 1)
            else:
                return self._recursiveHelper(array, target, mid + 1, right)
        else:
            if target > potentialmatch and target <= rightNum:
                return self._recursiveHelper(array, target, mid + 1, right)
            else:
                return self._recursiveHelper(array, target, left, mid - 1)

    # O(log(n)) time | O(1) space
    def iterative(self, array, target):
        left, right = 0, len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            potentialmatch = array[mid]
            leftNum = array[left]
            rightNum = array[right]
            if potentialmatch == target:
                return mid
            elif leftNum <= potentialmatch:
                if target < potentialmatch and target >= leftNum:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > potentialmatch and target <= rightNum:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

if __name__ == "__main__":
    array = [44, 61, 71, 72, 73, 0, 1, 21, 33, 43]
    s = Solution()
    print(s.recursive(array, 43))
    print(s.iterative(array, 43))