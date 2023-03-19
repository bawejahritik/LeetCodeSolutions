class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxCurr = 0;
        int maxSum = INT_MIN;
        
        for(int i=0; i<nums.size(); i++){
            maxCurr += nums[i];
            
            if(maxSum < maxCurr) maxSum = maxCurr;
            
            if(maxCurr < 0) maxCurr = 0;
        }
        
        return maxSum;
    }
};