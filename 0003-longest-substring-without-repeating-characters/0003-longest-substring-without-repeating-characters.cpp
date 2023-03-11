class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size() < 2) return s.size();
        
        unordered_map<char,int> count;
        int li = 0;
        int ri = 0;
        int ans = 0;
        
        while(ri < s.size()){
            // cout<<"check "<<count.find(s[ri]) == count.end()<<endl;
            if(count[s[ri]] == 0){
                cout<<"insert "<<s[ri]<<endl;
                count[s[ri]]++;
                ri++;
            }else{
                cout<<"remove "<<s[li]<<endl;
                count[s[li]]--;
                if(count[s[li]] == 0) count.erase(s[li]);
                li++;
            }
            
            ans = max(ri-li, ans);
        }
        
        return ans;
    }
};