class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> prevRow(1, 1);
        
        if(rowIndex == 0) return prevRow;
        
        for(int i=1; i<=rowIndex; i++){
            vector<int> currRow(i+1, 1);
            for(int j=1; j<i; j++){
                currRow[j] = prevRow[j-1] + prevRow[j];
            }
            prevRow = currRow;
        }
        
        return prevRow;
    }
};