class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> umap;
        int maxLength = 0;
        
        for(int i=0; i<s.size(); i++){
            umap[s[i]]++;
        }
        
        for(int i=0; i<s.size(); i++){
            if(umap[s[i]] % 2 == 0){
                maxLength += umap[s[i]];
                umap.erase(s[i]);
            }else if(umap[s[i]] > 2){
                maxLength += 2;
                umap[s[i]] -= 2;
            }
        }
        
        if(umap.empty()) return maxLength;
        else return maxLength + 1;
    }
};