class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        
        j = 0
        i = 0
        
        temp = [1] * len(nums)
        if(temp == nums):
            return len(nums)-1
        
        while(j < len(nums)):
            if(nums[j] != 0):
                j += 1
            elif(count == 0):
                j += 1
                count += 1
            else:
                while(nums[i] != 0):
                    i += 1
                i += 1
                count -= 1
            ans = max(ans, j-i-1)

        return ans
