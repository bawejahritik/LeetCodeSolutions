class Solution {
public:
    vector<vector<int>> ans;
    void backtrack(int n, int k, int start, vector<int> &temp){
        if(temp.size() == k){
            ans.push_back(temp);
            return;
        }
        
        for(int i=start; i<=n; i++){
            temp.push_back(i);
            backtrack(n, k, i+1, temp);
            temp.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        vector<int> temp;
        backtrack(n, k, 1 , temp);
        
        return ans;
        
    }
};