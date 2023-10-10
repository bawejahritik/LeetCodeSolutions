class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        
        maxLen = 0
        distinct = set()
        
        left = 0
        
        for right in range(len(s)):
            while s[right] in distinct:
                distinct.remove(s[left])
                left += 1
            
            distinct.add(s[right])
            
            maxLen = max(maxLen, right-left+1)
            
            
        
        
        return maxLen
        
        