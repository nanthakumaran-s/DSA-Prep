class Solution:
    def countInversion(self, array, temp, left, right):
        mid = inv = 0
        if left < right:
            mid = (left + right) // 2
            inv += self.countInversion(array, temp, left, mid)
            inv += self.countInversion(array, temp, mid + 1, right)

            self._merge(array, temp, left, mid + 1, right)
        return inv

    def _merge(self, array, temp, left, mid, right):
        i, j, k, inv = left, mid, left, 0
        while i <= mid - 1 and j <= right:
            if array[i] <= array[j]:
                temp[k] = array[i]
                i += 1
                k += 1
            else:
                temp[k] = array[j]
                inv = inv + (mid - i)
                j += 1
                k += 1

        while i <= mid -1:
            temp[k] = array[i]
            i += 1
            k += 1

        while j <= right:
            temp[k] = array[j]
            j += 1
            k += 1

        for i in range(left, right + 1):
            array[i] = temp[i]
        
        return inv

if __name__ == "__main__":
    arr = [1, 20, 6, 4, 5]
    temp = [0] * len(arr)
    print(Solution().countInversion(arr, temp, 0, len(arr) - 1))