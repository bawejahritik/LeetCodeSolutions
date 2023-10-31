class Solution:  
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        similar = collections.defaultdict(list)
        
        for str in strs:
            temp = [0]*26
            for s in str:
                temp[ord(s)-ord('a')] += 1
            
            similar[tuple(temp)].append(str)
        
        
        
        
        return similar.values()