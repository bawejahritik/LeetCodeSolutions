class Solution {
public:
    vector<int > dir = {0,1,0,-1,0};
    int orangesRotting(vector<vector<int>>& grid) {
            int m = grid.size();
    int n = grid[0].size();

    int minutes = 0;

    int freshOranges = 0;

    queue<pair<int,int>> q;

    for(int i=0; i<m; i++)
    {
        for(int k=0; k<n; k++)
        {
           if(grid[i][k]==2) q.push({i,k});
           if(grid[i][k]==1) freshOranges++; 
        } 
    }

    int count = q.size();

    while(q.empty() == false)
    {
        int row = q.front().first;
        int col = q.front().second;

        q.pop();

        grid[row][col] = 0;

        for(int i=0; i<4; i++)
        {
            int a = row+dir[i+1];
            int b = col+dir[i];
            if(a>=0 && a<m && b>=0 && b<n && grid[a][b] == 1)
            {
                 q.push({a,b});
                 grid[a][b] = 2;
                 freshOranges--;
            }  
        }

        if(--count == 0)
        {
            if(q.size()>0) minutes++;
            count = q.size();
        }


    }

    cout<<freshOranges<<" ";

    return freshOranges==0 ? minutes : -1;
    }
};