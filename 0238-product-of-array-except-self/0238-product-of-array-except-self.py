class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        
        curr1, curr2 = 1, 1
        
        for i in range(0, len(nums)):
            curr1 *= nums[i]
            curr2 *= nums[len(nums)-1-i]
            left.append(curr1)
            right.append(curr2)
        
        res = []
        
        right.reverse()
        
        res.append(right[1])
        
        for i in range(1, len(nums)-1):
            res.append(left[i-1]*right[i+1])
        
        res.append(left[-2])
        
        
        return res