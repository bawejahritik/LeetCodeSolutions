class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        topR, bottomR = 0, len(matrix)-1
        
        while topR<=bottomR:
            mid = (topR+bottomR)//2
            
            if matrix[mid][0] <= target:
                topR=mid+1
            else:
                bottomR = mid-1
        
        left, right = 0, len(matrix[0])-1
        
        while left<=right:
            mid = (left+right)//2
            
            if matrix[bottomR][mid] == target:
                return True
            elif matrix[bottomR][mid] < target:
                left = mid+1
            else:
                right = mid-1
        
        
        return False