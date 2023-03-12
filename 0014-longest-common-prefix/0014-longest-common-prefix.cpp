class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res ="";
        
        sort(strs.begin(), strs.end());
        
        for(int i=0; i<strs[0].size(); i++){
            char curr = strs[0][i];
            int j = 1;
            while(j < strs.size()){
                if(strs[j][i] != curr)break;
                else j++;
            }
            
            if(j == strs.size()){
                res += curr;
            }else{
                break;
            }
        }
        
        return res;
    }
};