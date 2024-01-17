class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = set()
        freq = {}
        
        for a in arr:
            freq[a] = 1 + freq.get(a, 0)
        
        for key, val in freq.items():
            if val in occurences:
                return False
            
            occurences.add(val)
        
        return True
        
        