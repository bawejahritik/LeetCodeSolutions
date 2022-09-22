class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        unordered_map<int, int> count;
        sort(nums.begin(), nums.end());
        
        vector<int> v;
        
        for(auto i : nums){
            if(count[i] == 0){
                count[i] = 1;
                v.push_back(i);
            }else{
                count[i]++;
            }
        }
        
        int n = v.size();
        
        if(n == 1){
            return v[0]*count[v[0]];
        }
        
        if(n == 2){
            if(v[0] + 1 == v[1]){
                return max(v[0]*count[v[0]], v[1]*count[v[1]]);
            }else{
                return v[0]*count[v[0]] + v[1]*count[v[1]];
            }
        }
        
        vector<int> dp(n, 0);
        dp[0] = v[0] * count[v[0]];
        
        
        if(v[0]+1 == v[1]){
            dp[1] = max(dp[0], v[1]*count[v[1]]);
        }else{
            dp[1] = dp[0] + v[1]*count[v[1]];
        }
        
        
        for(int i=2; i<n; i++){
            if(v[i] == v[i-1] + 1){
                dp[i] = max(dp[i-1], (v[i]*count[v[i]])+dp[i-2]);
            }else{
                dp[i] = dp[i-1] + (v[i]*count[v[i]]);
            }
        }
        
        return dp[n-1];
    }
};