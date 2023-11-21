class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        idx = -1
        
        def feasible(k, h):
            total_hrs = 0
            
            for p in piles:
                total_hrs += ceil(float(p)/k)
            
            return total_hrs <= h
        
        while left<=right:
            mid = (left+right)//2
            
            if feasible(mid, h):
                right = mid-1
                idx = mid
            else:
                left = mid+1
        return idx