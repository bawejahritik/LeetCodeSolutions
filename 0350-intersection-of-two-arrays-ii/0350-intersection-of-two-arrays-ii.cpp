class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        if(nums1.size() < nums2.size()){
            unordered_map<int, int> check1;
            vector<int> ans;
            
            for(int i=0; i<nums1.size(); i++){
                if(check1[nums1[i]] == 0){
                    check1[nums1[i]] = 1;
                }else{
                    check1[nums1[i]]++;
                }
            }
            
            for(int i=0; i<nums2.size(); i++){
                if(check1[nums2[i]] > 0){
                    check1[nums2[i]]--;
                    ans.push_back(nums2[i]);
                }
            }
            
            return ans; 
        }
        
        unordered_map<int, int> check2;
        vector<int> ans;
            
        for(int i=0; i<nums2.size(); i++){
                if(check2[nums2[i]] == 0){
                    check2[nums2[i]] = 1;
                }else{
                    check2[nums2[i]]++;
                }
            }
            
            for(int i=0; i<nums1.size(); i++){
                if(check2[nums1[i]] > 0){
                    check2[nums1[i]]--;
                    ans.push_back(nums1[i]);
                }
            }
            
            return ans; 
        
    }
};