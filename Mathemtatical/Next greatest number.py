class Solution:
    # O(n) time | O(1) space
    def nextGreatestNumber(self, number):
        number = [int(num) for num in str(number)]

        idx = -1

        for i in reversed(range(len(number))):
            if number[i] > number[i - 1]:
                idxToSwap = i - 1
                break

        if idx == -1:
            return -1

        for i in reversed(range(idxToSwap + 1, len(number))):
            if number[i] > number[idxToSwap]:
                idxToSwapWith = i
                break

        self._swap(idxToSwap, idxToSwapWith, number)

        left = idxToSwap + 1
        right = len(number) - 1

        while left < right:
            self._swap(left, right, number)
            left += 1
            right -= 1

        return int("".join(map(str, number)))


    def _swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

if __name__ == "__main__":
    s = Solution()
    print(s.nextGreatestNumber(2147483486))