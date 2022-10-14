class Solution {
public:
    bool isSubsequence(string s, string t) {
        int c1 = 0;
        int c2 = 0;
        
        while(c1 < s.size() && c2 < t.size()){
            if(s[c1] == t[c2]){
                c1++;
            }
            c2++;
        }
        
        return c1 == s.size();
    }
};