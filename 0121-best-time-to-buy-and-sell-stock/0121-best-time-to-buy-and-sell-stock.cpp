class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int minStock = prices[0];
        
        for(int i=1; i<prices.size(); i++){
            profit = max(profit, prices[i]-minStock);
            minStock = min(minStock, prices[i]);
        }
        
        return profit;
    }
};