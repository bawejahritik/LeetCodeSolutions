class Solution {
public:
    int findElements(vector<int>&nums, int i){
        int count = 0;
        for(int j = 0; j<nums.size(); j++){
            if(nums[j] >= i){
                count++;
            }
        }
        
        return count;
    }
    int specialArray(vector<int>& nums) {
        int maxX = nums.size();
        
        for(int i=0; i<=maxX; i++){
            int count = findElements(nums, i);
            if(count == i) return i;
        }
        
        return -1;
    }
};