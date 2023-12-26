class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        
        dp = [[-1]*(target+1) for _ in range(n+1)]
        
        def helper(n, k, target):
            if n==0 and target==0:
                return 1
            if n==0 or target<=0:
                return 0
            
            if dp[n][target]!=-1:
                return dp[n][target] % mod
            
            res = 0
            
            for i in range(1, k+1):
                res = (res + helper(n-1, k, target-i))%mod
            
            dp[n][target]=res%mod
            return dp[n][target]
        
        return helper(n, k, target)
        
        
            
            