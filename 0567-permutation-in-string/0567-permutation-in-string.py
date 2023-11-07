class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        
        ls1 = [0] * 26
        ls2 = [0] * 26
        
        for i in range(len(s1)):
            ls1[ord(s1[i]) - ord('a')] += 1
            ls2[ord(s2[i]) - ord('a')] += 1
        
        if ls1 == ls2:
            return True
        
        left = 0
        
        for right in range(len(s1), len(s2)):
            ls2[ord(s2[right]) - ord('a')] += 1
            ls2[ord(s2[left]) - ord('a')] -= 1
            left += 1
            
            if ls1==ls2:
                return True
        
        
        return False
        