class Solution {
public:
    int longestPalindrome(vector<string>& words) {
    
        bool sameletters = false;
        int count = 0;
        vector<vector<int>> store(26, vector<int>(26));
        
        for(int i=0; i<words.size(); i++){
            store[words[i][0]-'a'][words[i][1]-'a']++;
        }
        
        for(int i=0; i<26; i++){
            if(store[i][i] % 2 == 0){
                count += store[i][i];
            }else{
                count += (store[i][i]-1);
                sameletters = true;
            }
        }
        
        for(int i=0; i<26; i++){
            for(int j=i+1; j<26; j++){
                count += 2*min(store[i][j], store[j][i]);
            }
        }
        
        if(sameletters) count=count+1;
        return 2*count;
    }
};