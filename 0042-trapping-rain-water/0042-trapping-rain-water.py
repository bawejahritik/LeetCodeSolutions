class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        
        maxL, maxR = height[0], height[-1]
        water = 0
        
        while l<r:
            if maxL<=maxR:
                l+=1
                maxL = max(maxL, height[l])
                water += (maxL-height[l])
            else:
                r -= 1
                maxR = max(maxR, height[r])
                water += (maxR - height[r])
            
        
        
        return water