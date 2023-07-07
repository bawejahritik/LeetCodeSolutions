class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        size = 0
        
        if(len(s) == 0 and len(t) == 0):
            return True
        
        if(len(t) == 0):
            return False
        
        if(len(s) == 0):
            return True
        
        for i in t:
            if(i == s[size]):
                size+=1
            
            if(size == len(s)):
                return True
            # print(i, s[size])
            # print(i)
        
        
        return size==len(s)
        