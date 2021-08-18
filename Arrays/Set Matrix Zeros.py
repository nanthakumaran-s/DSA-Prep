class Solution:
    # O(m * n) time | O(m + n) space
    def better(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dummyrow = [-1] * m
        dummycol = [-1] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dummyrow[i] = 0
                    dummycol[j] = 0
        
        for i in range(m):
            for j in range(n):
                if dummyrow[i] == 0 or dummycol[j] == 0:
                    matrix[i][j] = 0
        
        return matrix

    # O(m * n) time | O(1) space
    def optimal(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        r = any(matrix[i][0] == 0 for i in range(m))
        c = any(matrix[0][j] == 0 for j in range(n))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] * matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if r:
            for i in range(m):
                matrix[i][0] = 0
        if c:
            for j in range(n):
                matrix[0][j] = 0
        
        return matrix
 
if __name__ == "__main__":
    matrix = [
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
    ]
    s = Solution()
    print(s.better(matrix))
    matrix2 = [
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
    ]
    print(s.optimal(matrix2))