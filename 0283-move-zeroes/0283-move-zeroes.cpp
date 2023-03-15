class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zero = 0;
        int i=0;
        
        while(i<nums.size()){
            if(nums[i] == 0) {
                zero++;
            }
            else if(zero > 0){
                nums[i-zero] = nums[i];
            }
            i++;
        }
        
        for(int i=nums.size()-zero; i<nums.size(); i++){
            nums[i]=0;
        }
        
    }
};