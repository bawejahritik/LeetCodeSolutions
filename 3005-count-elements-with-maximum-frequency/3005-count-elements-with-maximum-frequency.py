class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        res = 0
        maxYet = 0
        
        freq = {}
        
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
            maxYet = max(maxYet, freq[num])
        
        for num in freq:
            if freq[num] == maxYet:
                res += maxYet
        
        return res