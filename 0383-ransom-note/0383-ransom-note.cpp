class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> counter(26, 0);
        
        for(int i=0; i<magazine.size(); i++){
            counter[magazine[i]-'a']++;
        }
        
        for(int i=0; i<ransomNote.size(); i++){
            if(counter[ransomNote[i]-'a'] == 0) return false;
            else counter[ransomNote[i]-'a']--;
        }
        
        return true;
    }
};