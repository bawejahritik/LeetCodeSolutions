class Solution {
public:
    
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> ans(2);
        int si = 0;
        int ei = numbers.size()-1;
        
        while(si < ei){
            if(numbers[si] + numbers[ei] == target){
                ans[0] = si+1;
                ans[1] = ei+1;
                return ans;
            }else if(numbers[si] + numbers[ei] < target){
                si++;
            }else{
                ei--;
            }
        }
        
        return ans;
    }
};