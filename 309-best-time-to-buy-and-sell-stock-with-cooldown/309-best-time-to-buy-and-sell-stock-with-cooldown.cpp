class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int cooldown = 0;
        int hold = INT_MIN;
        int sell = 0;
        
        for(int i : prices){
            int prevCooldown = cooldown;
            int prevHold = hold;
            int prevSell = sell;
            
            cooldown = max(prevCooldown, prevSell);
            sell = prevHold + i;
            hold = max(prevHold, prevCooldown - i);
        }
        
        return max(sell, cooldown);
            
    }
};