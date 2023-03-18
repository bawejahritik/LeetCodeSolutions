class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int sum = 0;
        
        for(int i = 0; i<arr.size(); i++){
            int temp = 0;
            for(int j=i; j<arr.size(); j++){
                temp += arr[j];
                if((j-i+1)%2 == 1) {
                    sum += temp;
                    //cout<<temp<<" ";
            }}
        }
        
        return sum;
    }
};