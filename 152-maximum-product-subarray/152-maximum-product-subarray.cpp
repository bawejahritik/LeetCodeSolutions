class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums[0];
        int currMax = 1;
        int currMin = 1;
        
        if(nums.size() == 0) return res;
        
        for(auto i : nums){
            if(i == 0){
                currMax = 1;
                currMin = 1;
                //continue;
            }
            
            int temp = currMax * i;
            
            currMax = max(i * currMax, max(i * currMin, i));
            currMin = min(temp, min(i * currMin, i));
            res = max(res, currMax);
        }
        
        return res;
    }
};