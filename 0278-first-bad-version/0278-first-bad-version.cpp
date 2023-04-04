// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int si = 1;
        int ei = n;
        int mid = (ei-si)/2;
        int ans = 0;
        
        while(si<=ei){
            if(isBadVersion(mid)){
                ans = mid;
                ei = mid-1;
            }else{
                si = mid+1;
            }
            mid = si + (ei-si)/2;
        }
        
        return ans;
    }
};