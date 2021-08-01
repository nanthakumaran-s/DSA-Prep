class Solution:
    # O(n) time | O(1) space
    def twoPointer(self, array, target):
        left, right = 0, len(array) - 1
        while left < right:
            leftNum = array[left]
            rightNum = array[right]
            if leftNum != target:
                left += 1
            elif rightNum != target:
                right -= 1
            elif leftNum == target and rightNum == target:
                return [left, right]
        return [-1, -1]

    # O(log(n)) time | O(log(n)) space
    def recursiveBinarySearch(self, array, target):
        finalRange = [-1, -1]
        self._recursiveHelper(array, target, 0, len(array) - 1, finalRange, True)
        self._recursiveHelper(array, target, 0, len(array) - 1, finalRange, False)
        return finalRange

    def _recursiveHelper(self, array, target, left, right, finalRange, goLeft):
        if left > right:
            return
        
        mid = (left + right) // 2
        potentialMatch = array[mid]

        if potentialMatch > target:
            self._recursiveHelper(array, target, left, mid - 1, finalRange, goLeft)
        elif potentialMatch < target:
            self._recursiveHelper(array, target, mid + 1, right, finalRange, goLeft)
        else:
            if goLeft:
                if mid == 0 or array[mid - 1] != target:
                    finalRange[0] = mid
                else:
                    self._recursiveHelper(array, target, left, mid - 1, finalRange, goLeft)
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    finalRange[1] = mid
                else:
                    self._recursiveHelper(array, target, mid + 1, right, finalRange, goLeft)

    # O(log(n)) time | O(1) space
    def iterativeBinarySearch(self, array, target):
        finalRange = [-1, -1]
        self._iterativeHelper(array, target, 0, len(array) - 1, finalRange, True)
        self._iterativeHelper(array, target, 0, len(array) - 1, finalRange, False)
        return finalRange

    def _iterativeHelper(self, array, target, left, right, finalRange, goLeft):
        while left <= right:
            mid = (left + right) // 2
            potentialMatch = array[mid]

            if potentialMatch > target:
                right = mid - 1
            elif potentialMatch < target:
                left = mid + 1
            else:
                if goLeft:
                    if mid == 0 or array[mid - 1] != target:
                        finalRange[0] = mid
                        break
                    else:
                        right = mid - 1
                else:
                    if mid == len(array) - 1 or array[mid + 1] != target:
                        finalRange[1] = mid
                        break
                    else:
                        left = mid + 1

if __name__ == "__main__":
    array = [3, 45, 45, 45, 45, 45, 45, 45, 67, 78]
    s = Solution()
    print(s.twoPointer(array, 45))
    print(s.recursiveBinarySearch(array, 45))
    print(s.iterativeBinarySearch(array, 45))