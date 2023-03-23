class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s == t) return true;
        
        if(s.size() != t.size()) return false;
        
        vector<int> counter(26, 0);
        
        for(int i=0; i<s.size(); i++){
            counter[s[i]-'a']++;
        }
        
        for(int i=0; i<t.size(); i++){
            if(counter[t[i]-'a'] == 0) return false;
            else counter[t[i] - 'a']--;
        }
        
        
        return true;
    }
};