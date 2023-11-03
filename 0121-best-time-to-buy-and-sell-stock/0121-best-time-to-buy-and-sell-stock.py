class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minYet = prices[0]
        res = 0
        
        for price in prices:
            res = max(res, price-minYet)
            minYet = min(minYet, price)
        
        
        return res