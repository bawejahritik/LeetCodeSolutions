class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtracking(idx, path):
            if idx == len(nums):
                res.append(path)
                return
            
            backtracking(idx+1, path)
            backtracking(idx+1, path+[nums[idx]])
            
        backtracking(0, [])
        
        return res