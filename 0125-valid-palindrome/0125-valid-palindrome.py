class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while left<right:
            if (s[left].isalpha() or s[left].isdigit()) and (s[right].isalpha() or s[right].isdigit()):
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
            elif not (s[left].isalpha() or s[left].isdigit()):
                left += 1
            else:
                right -= 1
        
        return True