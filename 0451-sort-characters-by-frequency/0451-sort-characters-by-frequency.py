class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
            
        
        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse = True))
        
        res = ""
        for key in sorted_freq.keys():
            res += key*sorted_freq[key]
        
        return res