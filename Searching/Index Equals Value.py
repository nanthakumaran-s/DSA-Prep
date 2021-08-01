class Solution:
    # O(log(n)) time | O(1) space
    def binarySearchMethod(self, array):
        left, right = 0, len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            potentialMatch = array[mid]
            if potentialMatch == mid:
                return potentialMatch
            elif potentialMatch > mid:
                right = mid - 1
            else:
                left = mid + 1
        return -1

if __name__ == "__main__":
    s =Solution()
    print(s.binarySearchMethod([-1, 0, 2, 4, 6, 10]))