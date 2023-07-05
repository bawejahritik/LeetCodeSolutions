class Solution {
public:
    string reverseWords(string s) {
        int i=0, j=s.size()-1, k =s.size();
        
        while(isspace(s[i])){
            i++;
        }
        
        while(isspace(s[j])){
            j--;
        }
        
        cout<<i<<j;
        
        int count = 0;
        while(j>=i){
            
            if(j == i){
                s += s.substr(j, count+1);
                break;
            }
            
            if(isspace(s[j])){
                s += s.substr(j+1, count);
                s += " ";
                count = 0;
                while(isspace(s[j])){
                    j--;
                }
            }else{
                count++;
                j--;
            }
            
        }
        
        
        return s.substr(k);
    }
};