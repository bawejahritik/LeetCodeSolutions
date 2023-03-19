class Solution {
public:
    int uniquePaths(int m, int n) {
//         vector<vector<int>> dp(m, vector<int> (n, 0));
        
//         for(int i=1; i<m; i++){
//             for(int j=1; j<n; j++){
//                 dp[i][j] = dp[i-1][j] + dp[i][j-1] + 1; 
//             }
//         }
        
        long ans = 1;
        
        for(int i=m+n-2, j=1; i>=max(m, n); i--, j++){
            ans = (ans*i)/j;
        }
        
        
        return ans;    
    }
};