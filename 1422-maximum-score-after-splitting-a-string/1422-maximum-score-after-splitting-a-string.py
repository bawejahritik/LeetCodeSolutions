class Solution:
    def maxScore(self, s: str) -> int:
        score = float('-inf')
        
        for i in range(1, len(s)):
            left, right = s[:i], s[i:]
            temp = 0
            
            for j in left:
                if j == '0':
                    temp += 1
            for j in right:
                if j == '1':
                    temp += 1
            
            score = max(temp, score)
        return score