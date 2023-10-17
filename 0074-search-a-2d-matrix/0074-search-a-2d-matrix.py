class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        topRow, bottomRow = 0, len(matrix)-1
        row = -1
        
        while topRow<=bottomRow:
            mid = (topRow+bottomRow)//2
            
            if(matrix[mid][0] == target):
                return True
            elif matrix[mid][0] < target:
                topRow = mid+1
            else:
                bottomRow = mid-1
        
        
        left, right = 0, len(matrix[0])-1
        
        while left<=right:
            mid = (left+right)//2
            
            if matrix[bottomRow][mid] == target:
                return True
            elif matrix[bottomRow][mid] < target:
                left = mid+1
            else:
                right = mid-1
        
        return False