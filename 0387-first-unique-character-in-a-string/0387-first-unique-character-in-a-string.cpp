class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> mp;
        
        for(int i=0; i<s.size(); i++){
            if(mp.find(s[i]) ==  mp.end()) {
                mp[s[i]] = i;
                //cout<<"insert " + to_string(s[i])<<endl;
            }
            else{ 
                mp[s[i]] = -1;
                //cout<<"erase " + to_string(s[i])<<endl;
            }
        }
        
        int minIdx = INT_MAX;
        
        for(auto i : mp){
            //cout<<i.first<<i.second<<" ";
            if(i.second != -1) minIdx = min(minIdx, i.second);
        }
        
        if(minIdx == INT_MAX) return -1;
        else return minIdx;
    }
};