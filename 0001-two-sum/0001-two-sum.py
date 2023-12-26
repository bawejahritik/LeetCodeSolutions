class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        
        for i, num in enumerate(nums):
            if target-num in counter.keys():
                return [i, counter[target-num]]
            
            counter[num] = i
        
        return [0, 0]