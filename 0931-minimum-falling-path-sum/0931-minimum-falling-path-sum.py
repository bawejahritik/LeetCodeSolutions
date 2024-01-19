class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        
        for i in range(1, N):
            for j in range(N):
                mid = matrix[i-1][j]
                left = matrix[i-1][j-1] if j>0 else float('inf')
                right = matrix[i-1][j+1] if j<N-1 else float('inf')   
                
                matrix[i][j] = matrix[i][j] + min(mid, left, right)
                
        return min(matrix[-1])
                
        
        