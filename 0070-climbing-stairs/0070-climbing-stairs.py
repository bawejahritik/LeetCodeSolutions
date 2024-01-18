class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [-1] * (n+1)
        
        steps[0] = 0
        steps[1] = 1
        
        if n == 1:
            return steps[n]
        
        steps[2] = 2
        
        if n <= 2:
            return steps[n]
        
        for i in range(3, n+1):
            steps[i] = steps[i-1] + steps[i-2]
        
        return steps[n]