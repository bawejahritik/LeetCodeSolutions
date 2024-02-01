class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            curr = nums[i:i+3]
            if abs(curr[0]-curr[-1]) <= k:
                res.append(curr)
            else:
                return []
        
        return res