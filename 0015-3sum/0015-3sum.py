class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        
        for i in range(0, len(nums)-2):
            
            if nums[i]>0:
                break
            
            left = i+1
            right = len(nums)-1
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            while left<right:
                total = nums[i] + nums[left] + nums[right]
                if total<0:
                    left += 1
                elif total>0:
                    right-=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left]==nums[left-1] and left<right:
                        left += 1
        
        print(res)
        
        return res