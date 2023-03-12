class Solution {
public:
    string longestPalindrome(string s) {
        int ans = 0;
        string a = "";
        
        for(int i=0; i<s.size(); i++){
            int li = i;
            int ri = i;
            
            while(li >= 0 && ri <s.size() && s[li] == s[ri]){
                if(ans < ri-li+1){
                    a = s.substr(li, ri-li+1);
                    ans = ri-li+1;
                }
                
                li -= 1;
                ri += 1;
            }
            
            li = i;
            ri = i+1;
            
            while(li >= 0 && ri <s.size() && s[li] == s[ri]){
                if(ans < ri-li+1){
                    a = s.substr(li, ri-li+1);
                    ans = ri-li+1;
                }
                
                li -= 1;
                ri += 1;
            }
            
            
        }
        
        return a;
    }
};