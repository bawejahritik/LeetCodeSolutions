class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        res = [0]*2
        
        while left<right:
            if numbers[left]+numbers[right]==target:
                res[0] = left+1
                res[1] = right+1
                return res
            elif numbers[left]+numbers[right]<target:
                left += 1
            else:
                right -= 1
        
        return res