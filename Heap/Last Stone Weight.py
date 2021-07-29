class Heap:
    def __init__(self, array):
        self.heap = self._buildHeap(array)
        self.length = len(self.heap)
    
    def _buildHeap(self, array):
        parentIdx = (len(array) - 2) // 2
        for curentIdx in reversed(range(parentIdx)):
            self._siftDown(curentIdx, len(array) - 1, array)
        return array
    
    def _siftUp(self, curentIdx, heap):
        parentIdx = (curentIdx - 1) // 2
        while curentIdx > 0 and heap[parentIdx] < heap[curentIdx]:
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

    def peak(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self._siftUp(len(self.heap) - 1, self.heap)

    def remove(self):
        self._swap(0, len(self.heap) - 1, self.heap)
        value = self.heap.pop()
        self.length -= 1
        self._siftDown(0, len(self.heap) - 1, self.heap)
        return value

    def _swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

class Solution:
    def __init__(self, array):
        self.maxHeap = Heap(array)

    def lastStoneWeight(self):
        while self.maxHeap.length > 1:
            self.maxHeap.peak()
            firstStone = self.maxHeap.remove()
            secondStone = self.maxHeap.remove()
            
            result = abs(firstStone - secondStone)
            if result != 0:
                self.maxHeap.insert(result)
        return self.maxHeap.peak()

if __name__ == "__main__":
    s = Solution([2, 7, 4, 10])
    print(s.lastStoneWeight())

