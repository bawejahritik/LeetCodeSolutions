class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n0 = 0
        n1 = 0
        n2 = 0
        
        for num in nums:
            if num==0:
                n0+=1
            elif num==1:
                n1+=1
            else:
                n2+=1
        
        idx = 0
        
        for i in range(0, n0):
            nums[idx] = 0
            idx+=1
        
        for i in range(0, n1):
            nums[idx] = 1
            idx+=1
        
        for i in range(0, n2):
            nums[idx] = 2
            idx+=1