class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         [1, 2, 3, 4]
#         [1 ,2, 6, 24]
#         [24, 24, 12, 4]
        
        left = []
        right = []
        currLeft = 1
        currRight = 1
        s = len(nums)-1
        
        for i in range(len(nums)):
            currLeft *= nums[i]
            currRight *= nums[s-i]
            left.append(currLeft)
            right = [currRight] + right
        
        output = [right[1]]
        
        for i in range(1, len(nums)-1):
            output.append(left[i-1] * right[i+1])
        
        output.append(left[-2])

        return output
        