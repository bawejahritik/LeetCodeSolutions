class Solution {
public:
    int getMaxF(vector<int>& counter){
        int count = 0;
        
        for(int i=0; i<26; i++){
            count = max(count, counter[i]);
        }
        
        return count;
    }
    int characterReplacement(string s, int k) {
        int ans = 0;
        
        vector<int> counter(26, 0);
        int li = 0;
        int ri = 0;
        int maxF = 0;
        
        while(ri < s.size()){
            counter[s[ri]-'A']++;
            maxF = max(maxF, counter[s[ri]-'A']);
            
            if((ri-li+1) - maxF > k){
                counter[s[li]-'A']--;
                li++;
            }
            
            ans = max(ans, ri-li+1);
            ri++;
            
            //cout<<ans<<" ";
        }
        
        return ans;
    }
};