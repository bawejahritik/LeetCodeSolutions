class Solution {
public:
    int ans = 0;
    void binarySearch(vector<int> &arr, int si, int ei, int target){
        int i = si;
        while(si <= ei){
            int mid = si + (ei-si)/2;
            //cout<<arr[mid]<<endl;
            if(arr[mid] >= target){
                si = mid+1;
                ans = max(ans, mid-i);
            }else{
                ei = mid-1;
            }
        }
    }
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int maxYet = 0;
        
        for(int i=0; i<nums1.size(); i++){
            binarySearch(nums2, i, nums2.size()-1, nums1[i]);
        }
        
        return ans;
    }
};