class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int ans = -1;
        int minDist = INT_MAX;
        
        for(int i=0; i<points.size(); i++){
            if(points[i][0] == x || points[i][1] == y){
                int dist = abs(x - points[i][0]) + abs(y - points[i][1]);
                if(minDist > dist){
                    minDist = dist;
                    ans = i;
                }
            }
        }
        
        return ans;
    }
};