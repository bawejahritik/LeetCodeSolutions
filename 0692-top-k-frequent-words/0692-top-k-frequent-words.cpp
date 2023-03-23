class Solution {
public:
    struct lambda {
        bool operator()(pair<string, int>& a, pair<string, int>& b){
            return a.second > b.second || (a.second == b.second && a.first < b.first);
        }  
    };
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> mp;
        vector<string> ans;
        
        for(int i=0; i<words.size(); i++){
            mp[words[i]]++;
        }
        
        priority_queue<pair<string, int>, vector<pair<string, int>>, lambda> pq;
        
        for(auto i : mp){
            pq.push({i.first, i.second});
            while(pq.size() > k) pq.pop();
        }
        
        while(k>0){
            ans.push_back(pq.top().first);
            pq.pop();
            k--;
        }
        
        reverse(ans.begin(), ans.end());
        
        return ans;
    }
};