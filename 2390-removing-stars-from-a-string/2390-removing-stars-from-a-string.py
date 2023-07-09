class Solution:
    def removeStars(self, s: str) -> str:
        ans = "";
        
        for i in s:
            if(i == '*'):
                ans = ans[:-1]
            else:
                ans += i
        
        
        return ans