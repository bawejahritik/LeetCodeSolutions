class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> counter;
        vector<int> ans(2);
        
        for(int i=0; i<nums.size(); i++){
            //cout<<nums[i]<<" ";
            if(counter.find(target-nums[i]) != counter.end()){
                ans[0] = counter[target-nums[i]];
                ans[1] = i;
                //cout<<ans[0]<<ans[1]<<" ";
                break;
            }
            
            counter[nums[i]] = i;
        }
        
        return ans;
    }
};