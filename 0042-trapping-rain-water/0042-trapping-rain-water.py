class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = height[0], height[-1]
        waterTrapped = 0
        
        left, right = 0, len(height)-1
        
        while left<right:
            if maxL <= maxR:
                left += 1
                maxL = max(maxL, height[left])
                waterTrapped += (maxL-height[left])
            else:
                right -= 1
                maxR = max(maxR, height[right])
                waterTrapped += (maxR-height[right])
        
        return waterTrapped