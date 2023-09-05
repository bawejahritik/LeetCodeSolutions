class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        first_idx = -1
        
        while(left <= right):
            mid = (left+right)//2
            if nums[mid]==target:
                first_idx = mid
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        
        left, right = 0, len(nums)-1
        last_idx = -1
        
        while(left <= right):
            mid=(left+right)//2
            if(nums[mid] == target):
                last_idx=mid
                left=mid+1
            elif nums[mid] < target:
                left=mid+1
            else:
                right=mid-1
        
        return (first_idx, last_idx)