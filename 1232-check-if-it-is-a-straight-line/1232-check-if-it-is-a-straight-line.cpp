class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        if(coordinates.size() == 2) return true;
        
        int x = (coordinates[1][0]-coordinates[0][0]);
        int y = (coordinates[1][1]-coordinates[0][1]);
        
        for(int i=1;i<coordinates.size()-1; i++){
            int nx = coordinates[i+1][0] - coordinates[i][0];
            int ny = coordinates[i+1][1] - coordinates[i][1];
            
            if(x * ny != y * nx) return false;
        }
        
        return true;
    }
};