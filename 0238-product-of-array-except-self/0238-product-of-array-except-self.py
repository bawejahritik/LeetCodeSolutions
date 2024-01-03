class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         1  2  6  24
#         24 24 12 4 

        left = []
    
        runningLeft = 1
        for num in nums:
            runningLeft *= num
            left.append(runningLeft)
        
        # print(left)
        
        right = []
        
        runningRight = 1
        for i in range(len(nums)-1, -1, -1):
            runningRight *= nums[i]
            right.append(runningRight)
            
        # print(right)
        right.reverse()
        res = []
        
        res.append(right[1])
        
        for i in range(1, len(nums)-1):
            res.append(left[i-1] * right[i+1])
        
        res.append(left[-2])
        
        return res