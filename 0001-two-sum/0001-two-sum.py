class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = {}
        ans = [0, 0]
    
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in lst:
                ans[0] = i
                ans[1] = lst[target-nums[i]]
                return ans
            else:
                lst[nums[i]] = i
        
        
        return ans