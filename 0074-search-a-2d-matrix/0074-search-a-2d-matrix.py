class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1
        
        while top<=bottom:
            mid = (top+bottom)//2
            
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                top=mid+1
            else:
                bottom=mid-1
        
        left = 0
        right = len(matrix[0])-1
        
        while left<=right:
            mid = (left+right)//2
            if matrix[bottom][mid] == target:
                return True
            elif matrix[bottom][mid]<target:
                left=mid+1
            else:
                right = mid-1
        
        return False