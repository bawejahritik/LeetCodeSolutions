class Solution {
public:
    void helper(vector<vector<int>>& img, int sr, int sc, int color, int prevColor){
        if(sr<0 || sr>=img.size() || sc<0 || sc>=img[0].size() || img[sr][sc]== color || img[sr][sc]!=                  prevColor){
            return;
        }
        
        img[sr][sc] = color;
        helper(img, sr-1, sc, color, prevColor);
        helper(img, sr+1, sc, color, prevColor);
        helper(img,sr, sc-1, color, prevColor);
        helper(img, sr, sc+1, color, prevColor);
    }
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int prevColor = image[sr][sc];
        
        if(color != prevColor) helper(image, sr, sc, color, prevColor);
        
        return image;
    }
};