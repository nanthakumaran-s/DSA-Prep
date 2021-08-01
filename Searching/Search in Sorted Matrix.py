class Solution:
    # O(m + n) time | O(1) space [n = rows, m = columns]
    def search(self, matrix, target):
        startRowIdx = 0
        endColIdx = len(matrix[0]) - 1

        while 0 <= endColIdx and startRowIdx < len(matrix):
            potentialEqual = matrix[startRowIdx][endColIdx]
            if potentialEqual == target:
                return [startRowIdx, endColIdx]
            elif potentialEqual > target:
                endColIdx -= 1
            elif potentialEqual < target:
                startRowIdx += 1
        
        return -1

if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45 ,1003],
        [99, 100, 103, 106, 110, 1004]
    ]
    s = Solution()
    print(s.search(matrix, 110))
