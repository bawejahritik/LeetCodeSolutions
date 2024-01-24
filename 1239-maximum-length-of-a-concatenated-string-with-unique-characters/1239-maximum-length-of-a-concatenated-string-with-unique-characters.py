class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def dfs(i, currString):
            if i==len(arr):
                return len(currString)
            
            res = -1
            flag = True
            for c in arr[i]:
                if c in currString or arr[i].count(c) > 1:
                    flag = False
                    break
            
            if flag:
                res = dfs(i+1, currString + arr[i])
            
            res = max(res, dfs(i+1, currString))
            
            
            return res
        
        return dfs(0, "")
                