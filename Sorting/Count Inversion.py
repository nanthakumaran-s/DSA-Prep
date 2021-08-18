class Solution:
    def countInversion(self, array, temp, left, right):
        mid = inv = 0
        while left < right:
            mid = (left + right) // 2
            inv += self.countInversion(array, temp, left, mid)
            inv += self.countInversion(array, temp, mid + 1, right)

            self._merge(array, temp, left, mid + 1, right)
        return inv

    def _merge(self, array, temp, left, right):


