class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minYet = prices[0]
        maxProfit = 0
        
        for price in prices:
            curr = price - minYet
            maxProfit = max(maxProfit, curr)
            
            minYet = min(minYet, price)
        
        
        return maxProfit