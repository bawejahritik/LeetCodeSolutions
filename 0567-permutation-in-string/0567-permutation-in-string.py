class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freqS1 = [0] * 26
        
        for s in s1:
            freqS1[ord(s) - ord('a')] += 1

        window_size = len(s1)
        window = [0] * 26
        
        for right in range(window_size):
            window[ord(s2[right]) - ord('a')] += 1
        
        if window == freqS1: return True
        
        left = 0
        
        for right in range(window_size, len(s2)):
            window[ord(s2[right]) - ord('a')] += 1
            window[ord(s2[left]) - ord('a')] -= 1
            
            left += 1

            if window == freqS1: return True

        return False
        