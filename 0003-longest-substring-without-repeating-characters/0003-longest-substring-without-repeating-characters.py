class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        
        maxLen = 1
        distinct = set()
        distinct.add(s[0])
        
        left = 0
        right = 1
        
        while right <len(s):
            if s[right] in distinct:
                distinct.remove(s[left])
                left+=1
            else:
                distinct.add(s[right])
                right += 1
            
            maxLen = max(maxLen, right-left)
            
        
        
        return maxLen
        
        