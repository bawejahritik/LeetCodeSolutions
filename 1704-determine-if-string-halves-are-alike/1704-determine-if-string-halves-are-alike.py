class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        
        count1 = 0
        count2 = 0
        
        i, j = 0, len(s)-1
        
        while i<j:
            if s[i] in vowels:
                count1 += 1
            if s[j] in vowels:
                count2 += 1
            
            i += 1
            j -= 1
            

        return count1==count2