class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        
        for i in range(0, len(nums)-2):
            left = i+1
            right = len(nums)-1
            
            while left<right:
                total = nums[i] + nums[left] + nums[right]
                if total<0:
                    left += 1
                elif total>0:
                    right-=1
                else:
                    temp = [0]*3
                    temp[0] = nums[i]
                    temp[1] = nums[left]
                    temp[2] = nums[right]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
                    left += 1
                    right -= 1
        
        print(res)
        
        return res