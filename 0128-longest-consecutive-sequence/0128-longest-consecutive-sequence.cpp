class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> hash;
        int longest = 0;
        int curr = 0;
        
        for(int i=0; i<nums.size(); i++) hash.insert(nums[i]);
        
        int i=0;
        
        while(i<nums.size()){
            if(hash.find(nums[i] - 1) != hash.end()){
                i++;
            }else{
                curr++;
                int k = nums[i]+1;
                while(hash.find(k) != hash.end()) {
                    curr++;
                    k++;
                }
                longest = max(curr, longest);
                curr = 0;
                i++;
            }
        }
        
        return longest;
        
    }
};