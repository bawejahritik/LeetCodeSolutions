class Solution {
public:
    int partitionString(string s) {
        set<char> counter;
    
        int ri = 0;
        int count = 0;
        
        while(ri < s.size()){
            if(counter.find(s[ri]) != counter.end()){
                counter.clear();
                count += 1;
                //cout<<"count "<<count<<endl;
            }
            
            counter.insert(s[ri]);
            ri++;
        }
        
        return count+1;
    }
};