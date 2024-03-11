class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        res = ""
        for i in s:
            if i in order:
                freq[i] = 1 + freq.get(i, 0)
            else:
                res += i

        for i in order:
            if i in freq:
                res = res + i*freq[i]
        
        
        return res