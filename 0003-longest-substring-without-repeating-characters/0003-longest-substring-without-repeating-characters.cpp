class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len = 0;
        int li = 0;
        int ri = 0;
        
        if(s.size() < 2) return s.size();
        
        unordered_map<char, int> counter;
        
        while(ri < s.size()){
            if(counter.find(s[ri]) == counter.end()){
                counter[s[ri]]++;
                ri++;
            }else{
                counter[s[li]]--;
                if(counter[s[li]] == 0) counter.erase(s[li]);
                li++;
            }
            
            len = max(len, ri-li);
        }
        
        return len;
    }
};