class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                currLen = 1
                
                while num + currLen in nums:
                    currLen += 1
                maxLen = max(currLen, maxLen)
            
        return maxLen