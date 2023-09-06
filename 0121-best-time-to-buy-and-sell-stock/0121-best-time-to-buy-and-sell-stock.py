class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minYet = prices[0]
        
        for price in prices:
            ans = max(ans, price-minYet)
            minYet = min(minYet, price)
        
        return ans