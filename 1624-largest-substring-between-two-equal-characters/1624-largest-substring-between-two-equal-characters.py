class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        lastIndex = {}
        res = -1
        
        for i, char in enumerate(s):
            if char in lastIndex:
                res = max(res, i-lastIndex[char]-1)
            else:
                lastIndex[char] = i
                
        return res