class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = currSum = sum(nums[:k])
        
        for j in range(k, len(nums)):
            currSum += nums[j] - nums[j-k]
            maxSum = max(maxSum, currSum)
            print(maxSum, currSum, j)
        
        return maxSum/k