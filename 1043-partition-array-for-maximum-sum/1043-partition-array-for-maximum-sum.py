class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}
        
        def dfs(i):
            if i in cache:
                return cache[i]
            
            curr_max = 0
            res = 0
            
            for j in range(i, min(len(arr), i+k)):
                curr_max = max(curr_max, arr[j])
                window_size = j-i+1
                res = max(res, dfs(j+1) + curr_max*window_size)
            
            cache[i] = res
            return res
        
        return dfs(0)