class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        res = float("-inf")
        
        nums.sort()
        
        sidesum = sum(nums[:2])
        largest_side = nums[2]
        
        if sidesum > largest_side:
            res = max(res, sidesum + largest_side)
        
        for i in range(3, len(nums)):
            sidesum += largest_side
            largest_side = nums[i]
            if sidesum > largest_side:
                res = max(res, sidesum + largest_side)
        
        return res if res != float("-inf") else -1