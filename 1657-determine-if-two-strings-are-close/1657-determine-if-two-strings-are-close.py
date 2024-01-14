class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        v1 = sorted([i for i in freq1.values()])
        v2 = sorted([i for i in freq2.values()])
        
        return v1==v2 and freq1.keys()==freq2.keys()
