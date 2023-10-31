class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [0]*2
        counter = {}
        
        for i,num in enumerate(nums):
            diff = target-num
            if diff in counter:
                return [i, counter[diff]]
            counter[num] = i
        
        
        return ans