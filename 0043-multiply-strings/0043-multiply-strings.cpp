class Solution {
public:
    string multiply(string num1, string num2) {
        
        if(num1 == "0" || num2 == "0") return "0";
        
        vector<int> ans(num1.size()+num2.size(), 0);
        
        // reverse(num1.begin(), num1.end());
        // reverse(num2.begin(), num2.end());
        
        for(int i=num1.size()-1; i>=0; i--){
            for(int j=num2.size()-1; j>=0; j--){
                ans[i+j+1] +=  (num1[i]-'0')*(num2[j]-'0');
                //cout<<ans[i+j]<<" ";
                ans[i+j] += ans[i+j+1]/10;
                ans[i+j+1] %= 10;
                cout<<i<<" "<<j<<" "<<ans[i+j]<<" "<<ans[i+j+1]<<endl;
            }
        }
        
        int i=0;
        while(ans[i] == 0) i++;
        
        string s = "";
        
        while(i<ans.size()){
            s += to_string(ans[i++]);
        }
        
        return s;
    }
    
};