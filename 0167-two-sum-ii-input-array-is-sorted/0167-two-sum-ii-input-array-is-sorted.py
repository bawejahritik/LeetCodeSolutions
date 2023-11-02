class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        res = [0, 0]
        
        while l<r:
            s = numbers[l]+numbers[r]
            if s ==target:
                res[0] = l+1
                res[1] = r+1
                break
            elif s<target:
                l+=1
            else:
                r -= 1
        
        return res