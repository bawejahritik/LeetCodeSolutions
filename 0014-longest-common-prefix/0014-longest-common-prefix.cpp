class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(), strs.end());
        
        string ans = "";
        
        for(int i=0; i<strs[0].size(); i++){
            int j = 1;
            while(j<strs.size()){
                if(strs[0][i] == strs[j][i]) j++;
                else break;
            }
            
            if(j==strs.size()) ans+=strs[0][i];
            else break;
            
        }
        
        return ans;
    }
};