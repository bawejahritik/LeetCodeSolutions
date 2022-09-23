class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int n = nums.size();
        
        int curr_max = 0;
        int max_sofar = INT_MIN;
        int sum = 0;
        
        for(int i=0; i<n; i++){
            curr_max += nums[i];
            sum += nums[i];
            
            if(max_sofar < curr_max) max_sofar = curr_max;
            
            if(curr_max < 0) curr_max = 0;
            
            //cout<<max<<" "<<curr_max<<" ";
        }
        
        int curr_min = nums[0];
        int min_sofar = nums[0];
        for(int i=1; i<n; i++){
            curr_min = min(nums[i], nums[i] + curr_min);
            min_sofar = min(curr_min, min_sofar);
        }
        
        if(min_sofar == sum) return max_sofar;
        
        
        cout<<min_sofar<<" "<<max_sofar<<" "<<sum<<endl;
        
        return max(max_sofar, sum-min_sofar);
    }
};