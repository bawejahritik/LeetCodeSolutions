class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        res = 0
        
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for key, val in freq.items():
            if val == 1:
                return -1
            
            res += ceil(val/3)
        
        return res