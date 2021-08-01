class Solution:
    # O(n) time | O(1) space [average and best]
    # O(n^2) time | O(1) space [worst]
    def quickSelect(self, array, k):
        position = k - 1
        # k - 1 for kth smallest idx
        # len(array) - k for kth largest idx
        return self._quickSelectHelper(array, 0, len(array) - 1, position)

    def _quickSelectHelper(self, array, startIdx, endIdx, position):
        while True:
            if startIdx > endIdx:
                raise Exception("Some err happens")
            
            pivotIdx = startIdx
            leftIdx = startIdx + 1
            rightIdx = endIdx

            while leftIdx <= rightIdx:
                if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                    self._swap(leftIdx, rightIdx, array)
                elif array[leftIdx] <= array[pivotIdx]:
                    leftIdx += 1
                else:
                    rightIdx -= 1
            
            self._swap(pivotIdx, rightIdx, array)
            if rightIdx == position:
                return array[rightIdx]
            elif rightIdx > position:
                endIdx = rightIdx - 1
            else:
                startIdx = rightIdx + 1

    def _swap(self, i, j, array):
        array[i], array[j] = array[j], array[i] 

if __name__ == "__main__":
    s = Solution()
    print(s.quickSelect([4, 19, 3, 45, 23, 14], 3))