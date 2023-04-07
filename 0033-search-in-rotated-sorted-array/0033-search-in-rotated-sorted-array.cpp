class Solution {
public:
    int search(vector<int>& nums, int target) {
        int si = 0;
        int ei = nums.size()-1;
        
        while(si <= ei){
            int mid = si + (ei-si)/2;
            
            if(nums[mid] == target) return mid;
            
            if(nums[si] <= nums[mid]){
                if(nums[si] > target || nums[mid] < target) si = mid+1;
                else ei = mid-1;
            }else{
                if(nums[ei] < target || target<nums[mid]) ei = mid-1;
                else si = mid+1;
            }
            
            //cout<<mid<<" ";
        }
        
        
        return -1;
    }
};