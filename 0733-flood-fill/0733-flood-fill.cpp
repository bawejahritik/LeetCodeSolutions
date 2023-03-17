class Solution {
public:
    void helper(vector<vector<int>>& image, int sr, int sc, int color, int newColor){
        if(sr < 0 || sr >= image.size() || sc < 0 || sc > image[0].size() || image[sr][sc] == newColor ||                       image[sr][sc] != color){
            return;
        }
        image[sr][sc] = newColor;
        helper(image, sr-1, sc, color, newColor);
        helper(image, sr, sc-1, color, newColor);
        helper(image, sr, sc+1, color, newColor);
        helper(image, sr+1, sc, color, newColor);
    }
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int prevColor = image[sr][sc];
        
        if(color != prevColor) helper(image, sr, sc, prevColor, color);
        
        return image;
    }
};