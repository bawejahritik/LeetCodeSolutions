class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minYet = prices[0]
        maxProfit = 0
        
        for price in prices:
            if price < minYet:
                minYet = price
            
            maxProfit = max(maxProfit, price-minYet)
        
        return maxProfit