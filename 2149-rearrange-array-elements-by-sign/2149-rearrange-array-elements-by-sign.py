class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negatives = []
        positives = []
        
        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
        curr = 0
        for i in range(len(negatives)):
            nums[curr] = positives[i]
            nums[curr+1] = negatives[i]
            curr += 2
        return nums