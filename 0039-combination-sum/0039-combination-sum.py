class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtracking(idx, sumYet, path):
            if sumYet == target:
                res.append(path)
                return
                
            for i in range(idx, len(candidates)):
                candidate = candidates[i]
                if sumYet + candidate <= target:
                    backtracking(i, sumYet + candidate, path+[candidate])
            
        
        backtracking(0, 0, [])
        
        return res