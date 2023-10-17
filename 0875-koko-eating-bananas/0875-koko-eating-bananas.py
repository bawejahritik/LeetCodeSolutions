class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        
        while left<=right:
            k = (left+right)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/k)
                
            if hours<=h:
                res = k
                right = k-1
            else:
                left = k+1
        return res