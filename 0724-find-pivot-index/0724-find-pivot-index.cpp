class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int leftSum = 0;
        int total = 0;
        for(int i=0; i<nums.size(); i++){
            total += nums[i];
        }
        
        for(int i=0; i<nums.size(); i++){
            int rightSum = total - leftSum - nums[i];
            if(rightSum == leftSum) return i;
            
            leftSum = leftSum + nums[i];
        }
        
        return -1;
    }
};