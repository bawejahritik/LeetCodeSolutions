class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        cache = {}
        
        def count(i, k, prev, prevCount):
            
            if (i, k, prev, prevCount) in cache:
                return cache[(i, k, prev, prevCount)]
            
            if k<0:
                return float('inf')
            
            if i == len(s):
                return 0
            
            if s[i] == prev:
                incr = 1 if prevCount in [1, 9, 99] else 0
                res = incr + count(i+1, k, prev, prevCount+1)
            else:
                res = min (
                    count(i+1, k-1, prev, prevCount),   #exclude
                    1 + count(i+1, k, s[i], 1) #include
                )
                
            cache[(i, k, prev, prevCount)] = res
            
            return res
        
        return count(0, k, "", 0)
                