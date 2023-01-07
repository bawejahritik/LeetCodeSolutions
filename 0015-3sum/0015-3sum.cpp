class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        vector<vector<int>> ans;
        
        for(int i=0; i<nums.size(); i++){
            int li = i+1;
            int ri = nums.size()-1;
            int sum = 0 - nums[i];
            
            if(i == 0 || (i > 0 && nums[i] != nums[i-1])){
            
            while(li < ri){
                if(nums[li] + nums[ri] == sum){
                    vector<int> temp;
                    temp.push_back(nums[i]);
                    temp.push_back(nums[li]);
                    temp.push_back(nums[ri]);
                    
                    ans.push_back(temp);
                    
                    while(li < ri && nums[li+1] == nums[li])li++;
                    while(li < ri && nums[ri-1] == nums[ri])ri--;
                    li++;
                    ri--;
                }else if(nums[li] + nums[ri] < sum) li++;
                else ri--;
            }
            }
            //while(i < nums.size() && nums[i] == nums[i++])i++;
        }
        
        
        return ans;
    }
};