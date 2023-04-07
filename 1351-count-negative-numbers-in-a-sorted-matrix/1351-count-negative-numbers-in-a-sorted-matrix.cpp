class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int count = 0;
        
        for(int i=0; i<m; i++){
            int si = 0;
            int ei = n-1;
            
            while(si <= ei){
                int mid = si + (ei-si)/2;
                
                if(grid[i][mid] < 0) ei = mid-1;
                else si = mid+1;
            }
            
            count += (n-si);
            
            // for(int j=0; j<n; j++){
            //     if(grid[i][j] < 0)count++;
            // }
        }
        
        return count;
    }
};