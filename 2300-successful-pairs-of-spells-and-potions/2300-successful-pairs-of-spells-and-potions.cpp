class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());
        vector<int> ans;
        
        for(int i=0; i<spells.size(); i++){
            int count = 0;
            int si= 0;
            int ei = potions.size()-1;
            
            while(si <= ei){
                int mid = si + (ei-si)/2;
                long long product = (long long)spells[i] * (long long)potions[mid];
                if( product >= success){
                    ei = mid-1;
                }else{
                    si = mid+1;
                }
            }
            
            ans.push_back(potions.size()-si);
        }
        
        return ans;
    }
};