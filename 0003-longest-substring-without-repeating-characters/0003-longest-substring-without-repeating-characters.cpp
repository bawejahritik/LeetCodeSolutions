class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> umap;
        int count = 0;
        
        int l=0, r=0;
        
        while(r < s.size()){
            if(umap.find(s[r]) != umap.end()){
                if(umap[s[r]] + 1 > l){
                    l = umap[s[r]] + 1;
                }
            }
            
            umap[s[r]] = r;
            count = max(r-l+1, count);
            r++;
        }
        
        return count;
    }
};