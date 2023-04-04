class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans(2, -1);
        int si = 0;
        int ei = nums.size()-1;
        
        while(si<=ei){
            int mid = si + (ei-si)/2;
            if(nums[mid] == target){
                int si = mid;
                int ei = mid;
                cout<<mid<<" ";
                while(si-1>=0 && nums[si-1] == target){
                    si--;
                }
                cout<<si;
                while(ei+1 < nums.size()&&nums[ei+1] == target){
                    ei++;
                }
                cout<<ei;
                ans[0] = si;
                ans[1] = ei;
                return ans;
            }else if(nums[mid]<target){
                si = mid+1;
            }else ei = mid-1;
        }
        
        return ans;
    }
};