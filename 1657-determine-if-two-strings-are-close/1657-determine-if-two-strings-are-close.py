class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        list1 = Counter(word1)
        list2 = Counter(word2)
        
        list1 = sorted(list1.values())
        list2 = sorted(list2.values())
        
        set1 = set(word1)
        set2 = set(word2)
        
        return (list1==list2 and set1==set2)