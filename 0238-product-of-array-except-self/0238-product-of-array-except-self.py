class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        right = [1] * len(nums)
        
        for i in range(1, len(nums)):
            output[i] = output[i-1]*nums[i-1]
            
        for i in reversed(range(0, len(nums)-1)):
            right[i] = right[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            output[i] = output[i] * right[i]
        
        return output