class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums = []
        counts = []
        
        for i in range(len(arr)):
            if(arr[i] not in nums):
                currCount = arr.count(arr[i])
                if currCount not in counts:
                    counts.append(currCount)
                else:
                    return False
                nums.append(arr[i])
        
        return True