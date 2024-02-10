class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for start in range(0, len(s)):
            for end in range(start, len(s)):
                curr = s[start:end+1]
                if curr == curr[::-1]:
                    count+=1
        
        return count