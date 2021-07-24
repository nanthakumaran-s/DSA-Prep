class Solution:
    # O(n) time | O(1) space
    def validate(self, array, sequence):
        mainPtr, sequencePtr = 0, 0
        while mainPtr < len(array) and sequencePtr < len(sequence):
            if array[mainPtr] == sequence[sequencePtr]:
                sequencePtr += 1
            mainPtr += 1
        return sequencePtr == len(sequence)

s = Solution()
array = [4, 15, 12, 10, 35, 23, 20]
sequence = [15, 10, 23]
print(s.validate(array, sequence))