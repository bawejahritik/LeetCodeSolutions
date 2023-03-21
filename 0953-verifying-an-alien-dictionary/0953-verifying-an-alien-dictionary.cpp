class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        vector<int> counter(26, 0);
        
        for(int i=0; i<order.size(); i++){
            counter[order[i]-'a'] = i;
        }
        
        bool ans = true;
        
        for(int i=1; i<words.size(); i++){
            string prev = words[i-1];
            string curr = words[i];
            
            int j=0;
            for(j; j<min(prev.size(), curr.size()); j++){
                if(curr[j] == prev[j]) continue;
                if(counter[prev[j]-'a'] < counter[curr[j] - 'a']) break;
                if(counter[prev[j]-'a'] > counter[curr[j]-'a']){
                    ans = false;
                    break;
                }
            }
            
            if(prev.size()>curr.size() && j==curr.size()) ans = false;
            
            if(ans == false)break;
        }
        
        return ans;
    }
};