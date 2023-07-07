class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        
        for i in range(0, k):
            if(s[i] in vowels):
                count += 1
        
        ans = count
        
        for i in range(k, len(s)):
            if(s[i] in vowels):
                count += 1
            if(s[i-k] in vowels):
                count -=1
            ans = max(ans, count)
        
        
        
        return ans