class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        
        l, r = 0, len(nums)-1
        
        while l<=r:
            num1 = nums[r]*nums[r]
            num2 = nums[l]*nums[l]
            if num2 < num1:
                res = [num1] + res
                r-=1
            else:
                res = [num2] + res
                l += 1
        return res