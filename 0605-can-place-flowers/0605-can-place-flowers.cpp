class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int count = 0;
        
        if(flowerbed.size() == 1 && flowerbed[0]==0){
            return 1>=n;
        }
        
        if(flowerbed[0] == 0 && flowerbed[1] == 0){
            count++;
            flowerbed[0] =1;
        }
        
        for(int i=1; i<flowerbed.size()-1; i++){
            if(flowerbed[i]==0 && flowerbed[i-1]==0 && flowerbed[i+1]==0) {
                count++;
                flowerbed[i]=1;
            }
        }
        
        if(flowerbed[flowerbed.size()-1] == 0 && flowerbed[flowerbed.size()-2] == 0){
            count++;
        }
        
        return count>=n;
    }
};