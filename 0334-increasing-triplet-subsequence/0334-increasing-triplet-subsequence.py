class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if(len(nums) < 3):
            return False
        leftMin = float('inf')
        mid = float('inf')
        
        for i in range(0, len(nums)):
            if(nums[i] <= leftMin):
                leftMin = nums[i]
            elif(nums[i] < mid):
                mid = nums[i]
            elif(nums[i] > mid):
                return True
            
        return False