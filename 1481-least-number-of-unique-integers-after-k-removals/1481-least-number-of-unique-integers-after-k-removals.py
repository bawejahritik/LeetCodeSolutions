class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for i in arr:
            freq[i] = 1 + freq.get(i, 0)
        
        sorted_freq = dict(sorted(freq.items(), key=lambda x:x[1]))
        count = len(sorted_freq)
        while k>0:
            for key, value in sorted_freq.items():
                while value > 0:
                    print(key, value, count, k)
                    value -= 1
                    k -= 1
                    if k == 0:
                        break
                if value == 0:
                    count -= 1
                if k == 0:
                    break
        return count