class Solution:
    # O(n) time | O(n) space (n is the number of elements)
    def spiralTraverseIterative(self, array):
        result = []
        startRow, startCol = 0, 0 
        endRow, endCol = len(array) - 1, len(array[0]) - 1
        while startRow <= endRow and startCol <= endCol:

            for col in range(startCol, endCol + 1):
                result.append(array[startRow][col])

            for row in range(startRow + 1, endRow + 1):
                result.append(array[row][endCol])

            for col in reversed(range(startCol, endCol)):
                result.append(array[endRow][col])

            for row in reversed(range(startRow + 1, endRow)):
                result.append(array[row][startCol])

            startRow += 1
            startCol += 1
            endRow -= 1
            endCol -= 1

        return result

    # O(n) time | O(n) space (n is the number of elements)
    def spiralTraverseRecursive(self, array):
        result = []
        self._spiralFill(array, result, 0, 0, len(array) - 1, len(array[0]) - 1)
        return result

    def _spiralFill(self, array, result, startRow, startCol, endRow, endCol):
        if startRow > endRow and startCol > endCol:
            return

        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            result.append(array[row][startCol])
        
        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1
        

        self._spiralFill(array, result, startRow, startCol, endRow, endCol)


s = Solution()
array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]
print(s.spiralTraverseIterative(array))
print(s.spiralTraverseRecursive(array))