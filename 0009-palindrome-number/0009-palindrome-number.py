class Solution:
    def isPalindrome(self, x: int) -> bool:
        text = str(x)
        return text == text[::-1]