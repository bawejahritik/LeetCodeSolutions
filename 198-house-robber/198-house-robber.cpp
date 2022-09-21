class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 1) return nums[0];
        
        vector<int> profit(n+1, 0);
        
        profit[0] = nums[0];
        profit[1] = max(profit[0], nums[1]);
        
        for(int i=2; i<n; i++){
            profit[i] = max(nums[i] + profit[i-2], profit[i-1]);
            cout<<profit[i]<<" ";
        }
        
        return profit[n-1];
    }
};