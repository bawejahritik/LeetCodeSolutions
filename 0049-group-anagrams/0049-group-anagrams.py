class Solution:
            
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for str in strs:
            temp = [0]*26
            
            for s in str:
                temp[ord(s)-97] += 1
            
            ans[tuple(temp)].append(str)
        
        return ans.values()
         