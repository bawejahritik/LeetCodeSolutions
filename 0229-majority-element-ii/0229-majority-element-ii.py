class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        
        e1 = float('inf')
        e2 = float('inf')
        c1 = 0
        c2 = 0
        
        for i in range(0, len(nums)):
            if c1==0 and nums[i]!=e2:
                e1=nums[i]
                c1 += 1
            elif c2==0 and nums[i]!=e1:
                e2=nums[i]
                c2 += 1
            elif nums[i]==e1:
                c1 += 1
            elif nums[i]==e2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        
        
        ans=[]
        c1, c2=0, 0
        
        for i in range(0, len(nums)):
            if nums[i]==e1:
                c1+=1
            if nums[i]==e2:
                c2+=1
        
        check = (len(nums)//3) + 1
        
        print(check)
        
        if c1>=check:
            ans.append(e1)
        
        if c2>=check:
            ans.append(e2)
            
        ans.sort()
        
        return ans
                