class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        for i in s:
            freq[i] = 1 + freq.get(i, 0)
            
        res = ""
        
        for i in order:
            if i in freq:
                res = res + i*freq[i]
        
        for key, val in freq.items():
            if key in res:
                continue
            else:
                res += key*val
        
        return res