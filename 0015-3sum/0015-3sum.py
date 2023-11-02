class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
#         -4, -1, -1, 0, 1, 2
        
        for i in range(0, len(nums)-2):
            l, r = i+1, len(nums)-1
            
            if(nums[i] > 0):
                break
                
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            target = 0 - nums[i]
            while l<r:
                s = nums[l] + nums[r]
                if s==target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        
        return res
            
            
        