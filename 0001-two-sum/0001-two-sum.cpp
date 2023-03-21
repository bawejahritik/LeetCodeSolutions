class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> counter;
        vector<int> ans;
        
        for(int i=0; i<nums.size(); i++){
            if(counter.find(target-nums[i]) != counter.end()){
                ans.push_back(counter[target-nums[i]]);
                ans.push_back(i);
                break;
            }
            
            counter[nums[i]] = i;
            
        }
        
        return ans;
    }
};