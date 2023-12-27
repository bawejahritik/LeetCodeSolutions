class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        maxYet = -float('inf')
        lastColor = ""
        
        for i, color in enumerate(colors):
            if color == lastColor:
                res += min(maxYet, neededTime[i])
                maxYet = max(maxYet, neededTime[i])
            else:
                lastColor = color
                maxYet = neededTime[i]

        return res