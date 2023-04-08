class Solution {
    int getIndex(vector<int> row){
        int si = 0;
        int ei = row.size()-1;
        
        while(si <= ei){
            int mid = si + (ei-si)/2;
            if(row[mid] == 0) ei = mid-1;
            else si = mid+1;
        }
        
        return si;
    }
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        
        int m = mat.size();
        int n = mat[0].size();
        
        priority_queue<pair<int, int>> pq;
        
        for(int i=0; i<m; i++){
          pq.push({getIndex(mat[i]), i});  
            if(pq.size() > k) pq.pop();
        }
        
        vector<int> ans;
        
        while(pq.size()){
            ans.push_back(pq.top().second);
            pq.pop();
        }
        
        reverse(ans.begin(), ans.end());
        
        return ans;
        
    }
};