class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        
        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            temp = mapper.get(tuple(freq), [])
            temp.append(s)
            mapper[tuple(freq)] = temp
        
        return mapper.values()