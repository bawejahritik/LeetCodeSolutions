class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = {}
        
        for word in words:
            for char in word:
                freq[char] = 1 + freq.get(char, 0)
        
        
        for key in freq.keys():
            if freq[key] % (len(words)) != 0:
                return False
        
        return True