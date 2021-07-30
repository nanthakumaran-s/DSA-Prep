class Heap:
    def __init__(self, array):
        self.heap = self._buildHeap(array)
        self.length = len(self.heap)

    def _buildHeap(self, array):
        lastParentIdx = (len(array) - 2) // 2
        for curentIdx in reversed(range(lastParentIdx)):
            self._siftDown(curentIdx, self.length - 1, array)
        return array

    def _siftUp(self, curentIdx, heap):
        parentIdx = (curentIdx - 1) // 2
        while curentIdx > 0 and heap[parentIdx] > heap[curentIdx]:
            self._swap(curentIdx, parentIdx, heap)
            curentIdx = parentIdx
            parentIdx = (curentIdx - 1) // 2

    def _siftDown(self, curentIdx, endIdx, heap):
        childOneIdx = curentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = curentIdx * 2 + 2 if curentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            if heap[idxToSwap] < heap[curentIdx]:
                self._swap(curentIdx, idxToSwap, heap)
                curentIdx = idxToSwap
                childOneIdx = curentIdx * 2 + 1
            else:
                break

    def peak(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self._siftUp(self.length - 1, self.heap)

    def remove(self):
        self._swap(0, self.length - 1, self.heap)
        value = self.heap.pop()
        self.length -= 1
        self._siftDown(0, self.length - 1, self.heap)
        return value

    def _swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

class Solution:
    def __init__(self, arrrays):
        self.heap = Heap([])
        self.mergedArray = self._merge(arrrays)

    def _merge(self, arrrays):
        startColIdx = 0
        endColIdx = len(arrrays[0]) - 1
        results = []
        while startColIdx <= endColIdx:
            startRowIdx = 0
            endRowIdx = len(arrrays) - 1
            while startRowIdx <= endRowIdx:
                self.heap.insert(arrrays[startRowIdx][startColIdx])
                startRowIdx += 1
            while self.heap.length > 1:
                results.append(self.heap.remove())
            startColIdx += 1
        return results

    def printArr(self):
        print(self.mergedArray)

# O(n*k*log(k)) time | O(N) space
# n = number of columns, k = number of rows, N = total number of elements in the matrix
if __name__ == "__main__":
    arrays = [
        [3, 5, 8, 10],
        [1, 3, 4, 6],
        [2, 3, 5, 9],
    ]
    s = Solution(arrays)
    s.printArr()