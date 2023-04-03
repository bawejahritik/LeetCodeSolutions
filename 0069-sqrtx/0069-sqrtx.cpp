class Solution {
public:
    int mySqrt(int x) {
        long i=0;
        while(i*i <= x){
            i = i+1;
            
        }
        
       if(i*i == x) return i;
        else return i-1;
    }
};