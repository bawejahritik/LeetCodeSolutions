class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_map<int, int> counter;
        
        for(int i=0; i<arr.size(); i++){
            if(counter.find(arr[i]*2) != counter.end()) return true;
            else if(arr[i]%2 == 0 && counter.find(arr[i]/2) != counter.end()) return true;
            
            counter[arr[i]]++;
        }
        
        return false;
    }
};