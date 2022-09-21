class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        
        if(n == 1) return nums[0];
        
        if(n == 2) return max(nums[0], nums[1]);
        
        vector<int> arr(n, 0);
        vector<int> arr2(n, 0);
        
        arr[0] = nums[0];
        arr2[0] = nums[1];
        arr[1] = max(nums[1], arr[0]);
        arr2[1] = max(nums[2], arr2[0]);
        
        for(int i=2; i<n-1; i++){
            arr[i] = max(nums[i]+arr[i-2], arr[i-1]);
        }
        
        for(int i=2; i<n-1; i++){
            arr2[i] = max(nums[i+1]+arr2[i-2], arr2[i-1]); 
        }
        
        return max(arr[n-2], arr2[n-2]);
    }
};