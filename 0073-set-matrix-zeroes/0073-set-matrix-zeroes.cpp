class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        queue<int> col;
        queue<int> row;
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(matrix[i][j] == 0){
                    col.push(j);
                    row.push(i);
                }
            }
        }
        
        while(!row.empty()){
            int curr = row.front();
            for(int i=0; i<n;i++){
                matrix[curr][i] = 0;
            }
            row.pop();
        }
        
        while(!col.empty()){
            int curr = col.front();
            for(int i=0; i<m; i++){
                matrix[i][curr] = 0;
            }
            col.pop();
        }
        
        
    }
};