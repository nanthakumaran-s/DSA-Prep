class Heap:
    def __init__(self, array):
        self.heap = array
        self.length = len(self.heap)
    
    def _siftUp(self, curentIdx, heap):
        parentIdx = (curentIdx - 1) // 2
        while curentIdx >0 and heap[curentIdx] < heap[parentIdx]:
            self._swap(curentIdx, parentIdx, heap)
            curentIdx = parentIdx
            parentIdx = (curentIdx - 1) // 2

    def _siftDown(self, curentIdx, endIdx, heap):
        childOneIdx = curentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = curentIdx * 2 + 2 if curentIdx * 2 + 2 <= endIdx else - 1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[curentIdx]:
                self._swap(idxToSwap, curentIdx, heap)
                curentIdx = idxToSwap
                childOneIdx = curentIdx * 2 + 1
            else:
                break

    def remove(self):
        self._swap(0, self.length - 1, self.heap)
        value = self.heap.pop()
        self.length -= 1
        self._siftDown(0, self.length - 1, self.heap)
        return value

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self._siftUp(self.length - 1, self.heap)

    def _swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

class Solution:
    def sort(self, array, k):
        heap = Heap(array[:k + 1])
        index = 0
        for i in range(k + 1, len(array)):
            heap.insert(array[i])
            array[index] = heap.remove()
            index += 1
        while heap.length:
            array[index] = heap.remove()
            index += 1
        return array

if __name__ == "__main__":
    s = Solution()
    print(s.sort([1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2))
