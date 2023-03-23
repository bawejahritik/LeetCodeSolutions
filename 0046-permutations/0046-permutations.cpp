class Solution {
    vector<vector<int>> ans;
public:
    void getPermut(vector<int> &nums, int idx){
        if(idx == nums.size()){
            ans.push_back(nums);
            return;
        }
        
        for(int i=idx; i<nums.size(); i++){
            swap(nums[idx], nums[i]);
            getPermut(nums, idx+1);
            swap(nums[idx], nums[i]);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        if(nums.size() == 1) return {nums};
        
        getPermut(nums, 0);
        
        return ans;
    }
};