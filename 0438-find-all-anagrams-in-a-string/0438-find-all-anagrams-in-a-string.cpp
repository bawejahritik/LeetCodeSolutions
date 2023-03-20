class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
       int matches = 0;
        string s1 = p;
        string s2 = s;
        
        if(s1.size() > s2.size()) return {};
        
        vector<int> counter1(26, 0);
        vector<int> counter2(26, 0);
        vector<int> ans;
        
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
            if(matches == 26){
                ans.push_back(li);
            }
            
            counter2[s2[ri]-'a']++;
            
            
            if(counter1[s2[ri]-'a'] == counter2[s2[ri]-'a']) matches++;
            else if(counter1[s2[ri]-'a']+1 == counter2[s2[ri]-'a']) matches--;
            
            counter2[s2[li]-'a']--;
            
            if(counter1[s2[li]-'a'] == counter2[s2[li]-'a']) matches++;
            else if(counter1[s2[li]-'a']-1 == counter2[s2[li]-'a'])matches--;
            
            ri++;
            li++;
        }
        
        if(matches == 26){
            ans.push_back(li);
        }
        
        return ans;
    }
};