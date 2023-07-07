class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        ans1 = []
        for num in nums1:
            if(num not in nums2 and num not in ans1):
                ans1.append(num)
        
        ans.append(ans1)
        
        
        ans2 = []
        
        for num in nums2:
            if(num not in nums1 and num not in ans2):
                ans2.append(num)
        
        ans.append(ans2)
        
        return ans