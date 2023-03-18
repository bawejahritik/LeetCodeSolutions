class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> counter;
        
        for(int i=0; i<nums.size(); i++){
            if(counter.find(nums[i]) != counter.end()){
                return true;
            }
            
            counter[nums[i]]++;
        }
        
        return false;
    }
};