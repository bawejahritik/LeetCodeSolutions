class Solution {
public:

    int trap(vector<int>& height) {
        int n = height.size();
        int waterTrapped = 0;
        int maxLeft = 0;
        int maxRight = 0;
        int l = 0;
        int r = n-1;
        
        while(l <= r){
            if(height[l] <= height[r]){
                if(height[l] >= maxLeft) maxLeft = height[l];
                else waterTrapped += (maxLeft - height[l]);
                
                l++;
            }else{
                if(height[r] >= maxRight) maxRight = height[r];
                else waterTrapped += (maxRight - height[r]);
                
                r--;
            }
        }
        
        
        return waterTrapped;
    }
};