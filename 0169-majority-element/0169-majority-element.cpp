class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int p = nums[0];
        int count = 1;

        for(int i=1; i<nums.size(); i++){
            if(p != nums[i]){
                if(count == 0){
                    p = nums[i];
                    count = 1;
                }else{
                    count--;;
                }
            }else{
                count++;
            }
        }

        return p;
    }
};