class Solution {
public:
    void bfs(int r, int c, vector<vector<char>> &grid, vector<vector<int>> &visited){
        int m = grid.size();
        int n = grid[0].size();
        visited[r][c] = 1;
        queue<pair<int, int>> q;
        q.push({r, c});
        
        int drow[] = {1, 0, -1, 0};
        int dcol[] = {0, 1, 0, -1};
        
        while(!q.empty()){
            int row = q.front().first;
            int col = q.front().second;
            q.pop();
            
            for(int i=0; i<4; i++){
                int nr = row + drow[i];
                int nc = col + dcol[i];
                
                if(nr >= 0 && nr < m && nc >= 0 && nc < n && visited[nr][nc] == 0 && grid[nr][nc] == '1'){
                    visited[nr][nc] = 1;
                    q.push({nr, nc});
                }
            }
            
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        if(grid.size() == 0) return 0;
        
        int m = grid.size();
        int n = grid[0].size();
        int ans = 0;
        vector<vector<int>> visited(m, vector<int>(n, 0));
        
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(visited[i][j] == 0 && grid[i][j] == '1'){
                    ans++;
                    bfs(i, j, grid, visited);
                }
            }
        }
        
        return ans;
    }
};