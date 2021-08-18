class Solution:
    def sort(self, array):
        left, mid, right = 0, 0, len(array) - 1
        while mid <= right:
            if array[mid] == 0:
                self._swap(mid, left, array)
                mid += 1
                left += 1
            elif array[mid] == 1:
                mid += 1
            else:
                self._swap(mid, right, array)
                right -= 1
        return array

    def _swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

if __name__ == "__main__":
    print(Solution().sort([0,1,1,1,0,2,0,2,2,1,2]))