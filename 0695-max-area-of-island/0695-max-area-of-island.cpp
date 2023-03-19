class Solution {
public:
    int getArea(vector<vector<int>> &grid, vector<vector<int>> &visited, int r, int c){
        int area = 0;
        int m = grid.size();
        int n = grid[0].size();
        
        queue<pair<int, int>> q;
        q.push({r, c});
        area++;
        
        visited[r][c] = 1;
        
        int drow[] = {1, 0, -1, 0};
        int dcol[] = {0, 1, 0, -1};
        
        while(!q.empty()){
            int row = q.front().first;
            int col = q.front().second;
            q.pop();
            
            for(int i=0; i<4; i++){
                int nr = row + drow[i];
                int nc = col + dcol[i];
                
                if(nr>=0 && nr<=m-1 && nc>=0 && nc<=n-1 && grid[nr][nc]==1 && visited[nr][nc]==0){
                    area += 1;
                    visited[nr][nc] = 1;
                    q.push({nr, nc});
                }
            }
            
        }
        cout<<area<<" "; 
        
        return area;
        
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        int m = grid.size();
        int n = grid[0].size();
        
        vector<vector<int>> visited(m, vector<int>(n, 0));
        
        for(int i=0; i<m; i++){
            for(int j=0; j<n;j++){
                if(visited[i][j] == 0 && grid[i][j] == 1){
                    int area = getArea(grid, visited, i, j);
                    maxArea = max(maxArea, area);
                }
            }
        }
        
        return maxArea;
    }
};