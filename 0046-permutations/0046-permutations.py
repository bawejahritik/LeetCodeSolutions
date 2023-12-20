class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtracking(count, path, used):
            if count == len(nums):
                res.append(path)
                return
            
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                
                used[i] = True
                backtracking(count+1, path + [num], used)
                used[i] = False
                
        
        used = [False] * len(nums)
        backtracking(0, [], used)
        
        return res