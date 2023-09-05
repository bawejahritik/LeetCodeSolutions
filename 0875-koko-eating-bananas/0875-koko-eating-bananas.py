class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish_eating(piles:List[int], h:int, mid:int)->bool:
            hours_used = 0
            for p in piles:
                hours_used += ceil(float(p)/mid)
            return hours_used<=h
        left, right = 1, 1000000000
        boundary_index = -1
        
        while(left<=right):
            mid = (left+right)//2
            if can_finish_eating(piles, h, mid):
                boundary_index = mid
                right = mid-1
            else:
                left=mid+1
        
        return boundary_index