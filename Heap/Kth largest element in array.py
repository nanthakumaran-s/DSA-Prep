class Heap:
    def __init__(self, comparisonFunc, array):
        self.heap = array
        self.comparisonFunc = comparisonFunc
        self.length = len(self.heap)

    def _siftUp(self, curentIdx, heap):
        parentIdx = (curentIdx - 1) // 2
        while curentIdx > 0 and self.comparisonFunc(heap[curentIdx], heap[parentIdx]):
            self._swap(curentIdx, parentIdx, heap)
            curentIdx = parentIdx
            parentIdx = (curentIdx - 1) // 2

    def _siftDown(self, curentIdx, endIdx, heap):
        childOneIdx = curentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = curentIdx * 2 + 2 if curentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and self.comparisonFunc(heap[childTwoIdx], heap[childOneIdx]):
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if self.comparisonFunc(heap[idxToSwap], heap[curentIdx]):
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
        value = self.heap.pop(0)
        self.length -= 1
        self._siftDown(0, self.length - 1, self.heap)
        return value

    def _swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

def MAX_HEAP_FUNC(a, b):
    return a > b

if __name__ == "__main__":
    heap = Heap(MAX_HEAP_FUNC, [])
    array = [4, 12, 56, 23, 10, 5]
    for num in array:
        heap.insert(num)

    for i in range(3 - 1):
        heap.remove()

    print(heap.peak())