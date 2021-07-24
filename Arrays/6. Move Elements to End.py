class Solution:
    def move(self, array, target):
        left, right = 0, 1
        while right < len(array):
            firstNum = array[left]
            secondNum = array[right]
            if firstNum != target:
                left += 1
                if left == right:
                    right += 1
            elif firstNum == target and secondNum == target:
                right += 1
            elif firstNum == target and secondNum != target:
                array[left], array[right] = array[right], array[left]
                left += 1
                right += 1
        return array


s = Solution()
array = [2, 4, 2, 2, 2, 2, 5, 7, 2, 2, 2, 5, 14, 2]
print(s.move(array, 2))