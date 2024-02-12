class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = 0
        curr_count = 0
        
        for num in nums:
            if curr == num:
                curr_count += 1
            elif curr_count == 0:
                curr = num
                curr_count = 1
            else:
                curr_count -= 1
        
        return curr