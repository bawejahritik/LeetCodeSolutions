class Solution {
        static bool cmp(int a, int b){
        if(__builtin_popcount(a) == __builtin_popcount(b)) return b>a;
        else return __builtin_popcount(a)<__builtin_popcount(b);
    }
public:
    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(), arr.end(), cmp);
        return arr;
    }
};