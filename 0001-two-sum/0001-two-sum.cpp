class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> temp = nums;
        vector<int> ans;
        int num1;
        int num2;
        
        sort(temp.begin(), temp.end());
        
        int i=0, j=temp.size()-1;
        
        while(i<j){
            int sum = temp[i] + temp[j];
            
            if(sum == target){
                num1 = temp[i];
                num2 = temp[j];
                break;
            }else if(sum > target){
                j--;
            }else{
                i++;
            }
        }
        
        for(int i=0; i<nums.size(); i++){
            if(nums[i] == num1 || nums[i] == num2){
                ans.push_back(i);
            }
        }


        return ans;
    }
};