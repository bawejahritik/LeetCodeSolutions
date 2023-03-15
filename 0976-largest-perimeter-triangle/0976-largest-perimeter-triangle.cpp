class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        if(nums.size() < 3) return 0;
        
        sort(nums.begin(), nums.end());
        
        int ans = 0;
        
        for(int i=nums.size()-3; i>=0; i--){
            if(nums[i] + nums[i+1] > nums[i+2]){
                ans = max(ans, nums[i]+nums[i+1]+nums[i+2]);
            }
        }
        
        return ans;
    }
};