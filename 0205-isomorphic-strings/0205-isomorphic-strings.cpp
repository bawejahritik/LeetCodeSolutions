class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> check;
        unordered_map<char, char> check1;
        
        for(int i=0; i<s.size(); i++){
                check[s[i]] = t[i];
                check1[t[i]] = s[i];
            
        }
        for(int i=0; i<s.size(); i++){
            if(check[s[i]] != t[i] || check1[t[i]] != s[i]) return false;
        }
        
        return true;
    }
};