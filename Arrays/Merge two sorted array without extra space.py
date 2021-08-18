class Solution:
    # O(n + m) time | O(1) space
    def sort(self, arr1, arr2):
        gap = len(arr1) + len(arr2)
        gap = self._gap(gap)
        n = len(arr1)
        m = len(arr2)

        while gap > 0:
            left = 0
            while left + gap < n:
                if arr1[left] > arr1[left + gap]:
                    self._swap(left, gap + left, arr1, arr1)
                left += 1
            right = gap - n if gap > n else 0
            while left < n and right < m:
                if arr1[left] > arr2[right]:
                    self._swap(left, right, arr1, arr2)
                left += 1
                right -= 1
            if right < m:
                left = 0
                while left + gap < m:
                    if arr2[left] > arr2[left + gap]:
                        self._swap(left, left + gap, arr2, arr2)
                    left += 1
            gap = self._gap(gap)

        return [arr1, arr2]


    def _gap(self, gap):
        if gap <= 1:
            return 0
        return (gap // 2) + (gap % 2)

    def _swap(self, i, j, arr1, arr2):
        arr1[i], arr2[j] = arr2[j], arr1[i]


if __name__ == "__main__":
    arr1 = [5, 2, 6, 1]
    arr2 = [3, 4]
    print(Solution().sort(arr1, arr2))