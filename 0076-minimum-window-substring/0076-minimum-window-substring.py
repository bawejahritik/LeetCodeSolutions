class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return t
        
        listT = {}
        
        for i in range(len(t)):
            listT[t[i]] = 1 + listT.get(t[i], 0)
        
        listS = {}
        left = 0
        res, resLen = [-1, -1], float("infinity")
        have, need = 0, len(listT)
        
        for right in range(len(s)):
            listS[s[right]] = 1 + listS.get(s[right], 0)
            
            if s[right] in listT and listS[s[right]] == listT[s[right]]:
                have += 1
            
            while(have == need):
                if right-left+1 < resLen:
                    resLen = right-left+1
                    res[0] = left
                    res[1] = right
                    
                listS[s[left]] -= 1
                
                if s[left] in listT and listS[s[left]] < listT[s[left]]:
                    have -= 1
                
                left += 1
        
        
        l, r = res 
        
        return s[l:r+1] if resLen != float("infinity") else ""
    
        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    