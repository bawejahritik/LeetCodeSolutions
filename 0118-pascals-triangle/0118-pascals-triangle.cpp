class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans(numRows);
        
        ans[0] = {1};
        
        if(numRows == 1) return ans;
        
        ans[1] = {1, 1};
        
        if(numRows == 2) return ans;
        
        for(int i=2; i<numRows; i++){
            vector<int> temp = ans[i-1];
            vector<int> newTemp(i+1);
            newTemp[0] = 1;
            for(int j=1; j<i;j++){
                newTemp[j] = temp[j-1] + temp[j];
            }
            newTemp[i] = 1;
            ans[i] = newTemp;
        }
        
        return ans;
        
        
    }
};