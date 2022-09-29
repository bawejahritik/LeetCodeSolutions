class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        int count = 0;
        int pCount = 0;
        int nCount = 0;
        
        for(int i : nums){
            if(i == 0){
                pCount = 0;
                nCount = 0; 
            }
            
            if(i < 0){
                int temp = pCount;
                pCount = nCount;
                nCount = temp;
            }
            if(pCount > 0 || i > 0) pCount++;
            if(nCount > 0 || i < 0) nCount++;
            
            count = max(count, pCount);
        }
        
        return count;
    }
};