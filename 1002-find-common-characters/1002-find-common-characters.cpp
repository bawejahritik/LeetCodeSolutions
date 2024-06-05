class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<int> count(26);
        vector<int> current(26);
        
        int size = words.size();
        
       for(int i=0; i<words[0].size(); i++){
           count[words[0][i] - 'a'] ++;
       }
        
        for(int i=1; i<size; i++){
            string currentWord = words[i];
            
            for(int j=0; j<currentWord.size(); j++){
                current[currentWord[j]-'a']++;
            }
            
            for(int k=0; k<26; k++){
                count[k] = min(count[k], current[k]);
                current[k] = 0;
            }
        }
       
        vector<string> res;
        
        for(int i=0; i<26; i++ ){
            for(int j=0; j<count[i]; j++)
            {res.push_back(string(1, i+'a'));}
        }
        
        return res;
    }
};