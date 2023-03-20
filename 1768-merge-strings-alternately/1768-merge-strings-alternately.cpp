class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int s1 = word1.size();
        int s2 = word2.size();
        int i=0;
        int j=0;
        string s = "";
        
        while(i<s1 && j<s2){
            s += word1[i++];
            s += word2[j++];
        }
        
        while(i<s1){
            s += word1[i++];
        }
        
        while(j<s2){
            s += word2[j++];
        }
        
        return s;
    }
};