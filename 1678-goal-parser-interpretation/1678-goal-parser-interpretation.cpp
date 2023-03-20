class Solution {
public:
    string interpret(string command) {
        string s = "";
        int i = 0;
        
        while(i < command.size()){
            if(command[i] == 'G'){
                s += "G";
                i++;
            }else{
                if(command[i+1] == ')'){
                    s += "o";
                    i = i+2;
                }else{
                    s += "al";
                    i = i+4;
                }
            }
        }
        
        return s;
    }
};