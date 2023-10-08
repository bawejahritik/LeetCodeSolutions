class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevElements = {}
        
        for i, num in enumerate(nums):
            diff = target-num
            
            if diff in prevElements:
                return [prevElements[diff], i]
            
            prevElements[num] = i