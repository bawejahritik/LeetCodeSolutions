class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        cache = {}
        
        def dfs(i, d, currSum):
            if i == len(jobDifficulty):
                return 0 if d==0 else 100000000
            
            if d == 0:
                return 100000000
            
            if (i, d, currSum) in cache:
                return cache[(i, d, currSum)]
            
            currSum = max(currSum, jobDifficulty[i])
            
            res = min(
                dfs(i + 1, d, currSum),
                currSum + dfs(i+1, d-1, -1)
            )
            
            cache[(i, d, currSum)] = res
            
            return res
            
        
        return dfs(0, d, -1)