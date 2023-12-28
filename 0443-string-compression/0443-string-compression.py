class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        s = ""
        
        for i in range(1, len(chars)):
            if chars[i-1] != chars[i]:
                s += chars[i-1]
                if count > 1:
                    s += str(count)
                count = 1
            else:
                count += 1
        
        s += chars[-1]
        if count > 1:
            s += str(count)
            
        for i in range(len(s)):
            chars[i] = s[i]
            
        return len(s)