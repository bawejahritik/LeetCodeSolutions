class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = False
        col = False
        col0 = False
        
        if matrix[0][0] == 0:
            row=True
            col0 = True
            col = True
            
        
        for i in range(0, len(matrix[0])):
            if(matrix[0][i] == 0):
                row = True
        
        for j in range(0, len(matrix)):
            if(matrix[j][0] == 0):
                col = True
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    matrix[j][i]=0
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        
        if row:
            for i in range(0, len(matrix[0])):
                matrix[0][i] = 0
        
        if col0 or col:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0
                
        
        print(matrix)