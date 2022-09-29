class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int maxYet = values[0]+0;
        int maxScore = 0;
        
        for(int i=1; i<values.size(); i++){
            maxScore = max(maxScore, maxYet+values[i]-i);
            
            if(maxYet <= values[i]+i){
                maxYet = values[i]+i;
            }
        }
        
        return maxScore;
        
        
    }
};