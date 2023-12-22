class Solution:
    def maxScore(self, s: str) -> int:
        score = float('-inf')
        numOfZeros = 0
        numOfOnes = 0
        
        for i in s:
            if i == '1':
                numOfOnes += 1
                
        
        for i in range(1, len(s)):
            if s[i-1] == '0':
                numOfZeros += 1
            else:
                numOfOnes -= 1
            score = max(score, numOfZeros+numOfOnes)
            
        return score