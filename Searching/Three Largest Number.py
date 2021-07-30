# O(n + klog(n)) time | O(k) space
class Heap:
    def __init__(self, array):
        self.heap = self._buildHeap(array)

    def _buildHeap(self, array):
        lastparentIdx = (len(array) - 2) // 2
        for curentIdx in reversed(range(lastparentIdx)):
            self._siftDown(curentIdx, len(array) - 1, array)
        return array

    def _siftUp(self, curentIdx, heap):
        parentIdx = (curentIdx - 1) // 2
        while curentIdx > 0 and heap[curentIdx] > heap[parentIdx]:
            self._swap(curentIdx, parentIdx, heap)
            curentIdx = parentIdx
            parentIdx = (curentIdx - 1) // 2

    def _siftDown(self, curentIdx, endIdx, heap):
        childOneIdx = curentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = curentIdx * 2 + 2 if curentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] > heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] > heap[curentIdx]:
                self._swap(curentIdx, idxToSwap, heap)
                curentIdx = idxToSwap
                childOneIdx = curentIdx * 2 + 1
            else:
                break

    def remove(self):
        self._swap(0, len(self.heap) - 1, self.heap)
        value = self.heap.pop()
        self._siftDown(0, len(self.heap) - 1, self.heap)
        return value

    def _swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

class Solution:
    def findThreeNumbers(self, array):
        heap = Heap(array)
        result = []
        for i in range(3):
            result.append(heap.remove())
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.findThreeNumbers([4, 100, 5, 56, 23, 43, 54]))