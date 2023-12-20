class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtracking(idx, sumYet, path):
            if sumYet == target:
                res.append(path)
                return
                
            if sumYet > target or idx == len(candidates):
                return
            
            backtracking(idx, sumYet+candidates[idx], path + [candidates[idx]])
            backtracking(idx+1, sumYet, path)
            backtracking(idx+1, sumYet+candidates[idx], path+[candidates[idx]])
            
        
        backtracking(0, 0, [])
        
        temp = []

        [temp.append(x) for x in res if x not in temp]
        
        return temp