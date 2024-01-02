class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = {}
        maxFreq = 0
        
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
            maxFreq = max(maxFreq, freq[num])
        
        res = []
        
        while maxFreq > 0:
            temp = []
            
            for key in freq:
                if freq[key] > 0:
                    temp.append(key)
                    freq[key] -= 1
            res.append(temp)
            maxFreq -= 1
            
        return res