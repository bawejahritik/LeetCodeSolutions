class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int m = mat.size();
        int n = mat[0].size();
        vector<vector<int>> ans(r, vector<int> (c));
        
        if(m*n != r*c) return mat;
        
        int i=0;
        int j=0;
        
        for(int a=0; a<m; a++){
            for(int b=0; b<n; b++){
                ans[i][j] = mat[a][b];
                if(j < c-1){
                    j++;
                }else{
                    i++;
                    j=0;
                }
            }
        }
        
        return ans;
    }
};