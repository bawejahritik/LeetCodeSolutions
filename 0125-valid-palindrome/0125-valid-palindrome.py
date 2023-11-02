class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s)-1
        
        while l<r:
            print(s[l], s[r])
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
                print("inside if")
            elif not s[l].isalnum():
                l += 1
                print("inside l", s[l].isalpha())
            elif not s[r].isalnum():
                r -= 1
                print("inside r")
            else:
                return False
        
        
        return True
    