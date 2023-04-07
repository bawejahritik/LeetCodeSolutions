class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        
        int si = 0;
        int ei = (n*m)-1;
        
        while(si <= ei){
            int mid = si + (ei-si)/2;
            if(matrix[mid/n][mid%n] == target) return true;
            else if(matrix[mid/n][mid%n] < target) si = mid+1;
            else ei = mid-1;
            
            //cout<<matrix[mid][0]<<" ";
        }
        
//         int ri = si-1;
        
//         si = 0;
//         ei = n-1;
//         cout<<endl<<"ri "<<ri<<endl;
        
//         while(si <= ei){
//             int mid = si + (ei-si)/2;
            
//             if(matrix[ri][mid] == target) return true;
//             else if(matrix[ri][mid] < target) si = mid+1;
//             else ei = mid-1;
//             cout<<matrix[ri][mid]<<" ";
//         }
        
        return false;
        
    }
};