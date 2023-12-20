class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        minSpent = float('inf')
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] + prices[j] <= money:
                    minSpent = min(minSpent, prices[i] + prices[j])
                    
        return money - minSpent if minSpent != float('inf') else money