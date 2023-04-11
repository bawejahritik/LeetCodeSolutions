class Solution {
public:
    int findMin(vector<int>& nums) {
        int si = 0;
        int ei = nums.size()-1;
        
        if(nums[0] < nums[ei]) return nums[0];
        
        if(nums.size() == 1) return nums[0];
        
        while(si <= ei){
            int mid = si + (ei-si)/2;
            
            if(nums[mid] > nums[mid+1]){
                return nums[mid+1];
            }
            
            if(nums[mid] < nums[mid-1]){
                return nums[mid];
            }
            
            if(nums[mid] > nums[0]) si = mid+1;
            else ei = mid-1;
        }
        
        return INT_MAX;
    }
};