class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int matches = 0;
        
        if(s1.size() > s2.size()) return false;
        
        vector<int> counter1(26, 0);
        vector<int> counter2(26, 0);
        
        for(int i=0; i<s1.size(); i++){
            counter1[s1[i]-'a']++;
            counter2[s2[i]-'a']++;
        }
        
        for(int i=0; i<26; i++){
            if(counter1[i] == counter2[i]) matches++;
        }
        
        int li=0;
        int ri=s1.size();
        
        while(ri < s2.size()){
            if(matches == 26) return true;
            
            counter2[s2[ri]-'a']++;
            
            
            if(counter1[s2[ri]-'a'] == counter2[s2[ri]-'a']) matches++;
            else if(counter1[s2[ri]-'a']+1 == counter2[s2[ri]-'a']) matches--;
            
            counter2[s2[li]-'a']--;
            
            if(counter1[s2[li]-'a'] == counter2[s2[li]-'a']) matches++;
            else if(counter1[s2[li]-'a']-1 == counter2[s2[li]-'a'])matches--;
            
            ri++;
            li++;
        }
        
        return matches==26;
    }
};