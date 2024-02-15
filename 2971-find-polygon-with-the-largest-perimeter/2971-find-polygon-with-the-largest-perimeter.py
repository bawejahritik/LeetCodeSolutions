class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        res = -1
        
        nums.sort()
        
        sidesum = 0
        
        
        for num in nums:
            if num < sidesum:
                res = sidesum + num
            sidesum += num
        
        return res