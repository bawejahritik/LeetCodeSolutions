class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int globalCount = 0;
        int localCount = 0;
        
        for(int i=0; i<nums.size(); i++){
            globalCount = max(localCount, globalCount);
            if(nums[i] == 1){
                localCount++;
            }else{
                localCount = 0;
            }
        }
        globalCount = max(localCount, globalCount);
        
        return globalCount;
    }
};