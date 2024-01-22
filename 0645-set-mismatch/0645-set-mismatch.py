class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        
        for i in range(1, len(nums)+1):
            if i not in nums:
                res[1] = i
                break
        
        total = (len(nums)/2) * (1 + len(nums))
        
        res[0] = int(sum(nums) - total + res[1])
        
        return res