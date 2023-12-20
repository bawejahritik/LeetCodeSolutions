class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        
        minCost = prices[0] + prices[1]
        
                    
        return money - minCost if minCost <= money else money