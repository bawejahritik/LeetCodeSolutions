class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "": return ""
        
        freqT = {}
        
        for i in t:
            freqT[i] = 1 + freqT.get(i, 0)
            
        have, need = 0 , len(freqT)
        freqS = {}
        
        res, resLen = [-1, -1], float("infinity")
        
        left = 0
        
        for right in range(len(s)):
            freqS[s[right]] = 1 + freqS.get(s[right], 0)
            
            if s[right] in freqT and freqS[s[right]] == freqT[s[right]]:
                have += 1
            
            while have == need:
                if right-left+1 < resLen:
                    res[0] = left
                    res[1] = right
                    resLen = right-left+1
                
                freqS[s[left]] -= 1
                
                if s[left] in freqT and freqS[s[left]] < freqT[s[left]]:
                    have -= 1
                
                left += 1
                
            
        return s[res[0]:res[1]+1] if resLen != float("infinity") else ""
        
        