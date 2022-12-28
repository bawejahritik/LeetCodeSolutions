class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int p1 = nums[0];
        int p2 = nums[0];
        int c1=1, c2=0;
        int n = nums.size();
        
        if(n < 2) return nums;
        
        vector<int> ans;
        
        for(int i=1; i<nums.size(); i++){
            if(p1 == nums[i]) c1++;
            else if(p2 == nums[i])c2++;
            else{
                if(c1 == 0){
                    p1 = nums[i];
                    c1++;
                }else if(c2 == 0){
                    p2 = nums[i];
                    c2++;
                }else{
                    c1--;
                    c2--;
                }
            }
        }
        
        int a = 0, b = 0;
        
        for(int i=0; i<nums.size(); i++){
            if(p1 == nums[i]) a++;
            else if(p2 == nums[i])b++;
        }
        
        if(a > (n/3)) ans.push_back(p1);
        
        if(b > (n/3)) ans.push_back(p2);
        
        
        return ans;
    }
};