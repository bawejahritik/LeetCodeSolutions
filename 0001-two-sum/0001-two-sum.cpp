class Solution {
public:
    
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans(2);
        unordered_map<int, int> umap;
        
        for(int i=0; i<nums.size(); i++){
            if(umap.find(target-nums[i]) != umap.end()){
                ans[0] = umap[target-nums[i]];
                ans[1] = i;
                break;
            }
            
            umap[nums[i]]=i;
        }
        
        return ans;
    }
};