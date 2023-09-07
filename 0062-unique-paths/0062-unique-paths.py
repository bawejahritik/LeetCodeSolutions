class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        temp = [0]*n
        matrix = [temp]*m
        
        for i in range(0, n):
            matrix[0][i] = 1
        
        for i in range(0, m):
            matrix[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        
        
        return matrix[m-1][n-1]
            