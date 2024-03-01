class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        number_of_ones = s.count('1')
        
        if number_of_ones == 1:
            return ("0" * (len(s)-1)) + "1"
        
        else:
            return "1"*(number_of_ones-1)+"0"*(len(s)-number_of_ones)+"1"
        
        return s