class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if majority == nums[i]:
                count += 1
            else:
                count -= 1
                if count==0:
                    majority = nums[i]
                    count = 1
        
        return majority