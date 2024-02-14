class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negatives = []
        positives = []
        
        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
        res = []
        for i in range(len(negatives)):
            res.append(positives[i])
            res.append(negatives[i])
        return res