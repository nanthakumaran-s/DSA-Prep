class Solution:
    # O(n * m) time | O(1) space
    def rotate(self, matrix):
        for i in range(len(matrix[0])):
            for j in range(i, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        row = 0
        endRow = len(matrix) - 1
    
        while row < endRow:
            matrix[row], matrix[endRow] = matrix[endRow], matrix[row]
            row += 1
            endRow -= 1

        # Clockwise
        # col = 0
        # endCol = len(matrix[0]) - 1
    
        # while col < endCol:
        #     row = 0
        #     endRow = len(matrix) - 1
        
        #     while row <= endRow:
        #         matrix[row][col], matrix[row][endCol] = matrix[row][endCol], matrix[row][col]
        #         row += 1
            
        #     col += 1
        #     endCol -= 1
        
        return matrix


A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

s = Solution()
print(s.rotate(A))