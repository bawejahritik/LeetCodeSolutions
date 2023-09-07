class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        
        if n<0:
            n = -1*n
            x = 1.0/x
        
        ans = 1
        
        while n!=0:
            if n%2==1:
                ans *= x
                n -= 1
            x *= x
            n//=2
                
                
        return ans