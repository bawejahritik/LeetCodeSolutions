class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        maxYet = -1
        for num in nums:
            if 0-num in seen:
                maxYet = max(maxYet, abs(num))
            seen.add(num)
        return maxYet