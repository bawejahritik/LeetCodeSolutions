class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int si = 0;
        int ei = letters.size()-1;
        
        while(si <= ei){
            int mid = si + (ei-si)/2;
            if(letters[mid] <= target) si = mid+1;
            else ei = mid-1;
            
            //cout<<si<<" "<<ei<<" "<<endl;
        }
        
        
        return letters[si%letters.size()];
    }
};