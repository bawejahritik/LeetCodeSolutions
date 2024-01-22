class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[-1 for _ in range(n)] for _ in range(m)]
        
        grid[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                elif i == 0 or j == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        
        
        return grid[m-1][n-1]