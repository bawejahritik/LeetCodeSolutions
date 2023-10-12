class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        countT, window = {}, {}
        
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        res, resLen = [-1, -1], float("infinity")
        have, need = 0, len(countT)
        
        left = 0
        
        for right in range(len(s)):
            c = s[right]
            
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need :
                if (right-left+1)<resLen:
                    res = [left, right]
                    resLen = right-left+1
                
                window[s[left]] -= 1
                
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                
                left += 1
        
        
        l, r = res
        
        return s[l:r+1] if resLen != float("infinity") else ""