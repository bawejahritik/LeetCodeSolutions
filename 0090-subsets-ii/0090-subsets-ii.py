class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(idx, path):
            if idx==len(nums):
                if path not in res:
                    res.append(path)
                
                return
            
            backtracking(idx+1, path + [nums[idx]])
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtracking(idx+1, path)
            
        backtracking(0, [])
        
        return res