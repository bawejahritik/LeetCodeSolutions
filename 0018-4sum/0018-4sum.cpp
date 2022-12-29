class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        
        if(nums.size() <= 3) return ans;
        
        for(int i=0; i<nums.size(); i++){
            for(int j=i+1; j<nums.size(); j++){
                int l = j+1, r = nums.size()-1;
                long long int c = nums[i] + nums[j];
                while(l < r){
                    if(nums[l] + nums[r] > target - c) r--;
                    else if(nums[l] + nums[r] < target - c) l++;
                    else{
                        vector<int> temp(4);
                        temp[0] = nums[i];
                        temp[1] = nums[j];
                        temp[2] = nums[l];
                        temp[3] = nums[r];
                        ans.push_back(temp);
                        
                        while(l < r && nums[l+1] == nums[l]) l++;
                        while(l < r && nums[r-1] == nums[r]) r--;
                        
                        l++;
                        r--;
                    }
                }
                while(j + 1 < nums.size() && nums[j+1] == nums[j]) j++;
            }
            while(i+1 < nums.size() && nums[i+1] == nums[i]) i++;
        }
        
        return ans;
    }
};