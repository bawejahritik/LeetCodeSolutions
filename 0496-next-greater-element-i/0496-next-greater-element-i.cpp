class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans;
        unordered_map<int, int> idx;
        
        for(int i=0; i<nums2.size()-1; i++){
            if(nums2[i] < nums2[i+1]) idx[nums2[i]] = nums2[i+1];
            else {
                int j = i+1;
                while(j < nums2.size()){
                    if(nums2[i] < nums2[j]){
                        idx[nums2[i]] = nums2[j];
                        break;
                    }else{
                        j++;
                    }
                }
                if(j == nums2.size()) idx[nums2[i]] = -1;
            }
        }
        
        idx[nums2[nums2.size()-1]] = -1;
        
        for(int i=0; i<nums1.size(); i++){
            ans.push_back(idx[nums1[i]]);
        }
        
        
        return ans;
    }
};