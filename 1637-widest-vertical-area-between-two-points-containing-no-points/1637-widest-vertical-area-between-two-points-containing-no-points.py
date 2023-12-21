class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        
        maxYet = float('-inf')
        res = 0
        
        for i in range(1, len(points)):
            pt1 = points[i-1][0]
            pt2 = points[i][0]
            
            if pt2-pt1 > maxYet:
                res = pt2-pt1
                maxYet = res
        
        return res