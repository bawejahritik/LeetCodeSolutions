class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtracking(idx, sumYet, path):
            if sumYet>target or idx == len(candidates):
                if sumYet==target:
                    res.append(path)
                return
            if sumYet == target:
                res.append(path)
                return
            
            backtracking(idx+1, sumYet+candidates[idx], path + [candidates[idx]])
            while(idx<len(candidates)-1 and candidates[idx+1] == candidates[idx]):
                idx += 1
            backtracking(idx+1, sumYet, path)   
            
            
        
        backtracking(0, 0, [])
        
        return res