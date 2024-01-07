class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(list(zip(startTime, endTime, profit)))
        
        cache = {}
        
        def dfs(i):
            if i==len(startTime):
                return 0
            
            if i in cache:
                return cache[i]
            
            res = dfs(i+1)
            
            left, right = i+1, len(startTime)-1
            
            while left <= right:
                mid = (left + right) // 2
                
                if intervals[mid][0] >= intervals[i][1]:
                    right = mid-1
                else:
                    left = mid+1
                    
            
            res = max(res, intervals[i][2] + dfs(left))
            
            
            cache[i] = res
            
            
            return res
            
        
        return dfs(0)
