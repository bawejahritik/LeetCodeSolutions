class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = float('-inf')
        curr_sum = 0
        
        for num in nums:
            curr_sum += num     
            largest_sum = max(curr_sum, largest_sum)
            
            if curr_sum < 0:
                curr_sum=0
        
        return largest_sum