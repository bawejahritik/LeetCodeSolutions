class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s1 = [0]*26
        t1 = [0]*26
        
        for i in range(len(s)):
            s1[ord(s[i])-ord('a')] += 1
            t1[ord(t[i])-ord('a')] += 1
            
        return s1 == t1