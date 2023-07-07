class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        ans = 0
        
        i,j = 0, 0
        
        while(j<len(nums)):
            if(nums[j] != 0):
                j += 1
            elif(count < k):
                j+=1
                count += 1
            else:
                while(count >= k):
                    if(nums[i] != 0):
                        i+=1
                    else:
                        count -= 1
                        i += 1
            # print(nums[i:j])
            ans = max(ans, j-i)
        
        
        return ans
        