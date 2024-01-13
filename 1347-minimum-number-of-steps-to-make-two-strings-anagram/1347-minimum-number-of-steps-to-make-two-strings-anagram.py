class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq1 = [0] * 26
        freq2 = [0] * 26
        for i in s:
            freq1[ord(i) - ord('a')] += 1
        
        
        for i in t:
            freq2[ord(i) - ord('a')] += 1
        
        res = 0
        
        for i in range(26):
            if freq1[i] > freq2[i]:
                res += (freq1[i] - freq2[i])
        
        
        return res
            