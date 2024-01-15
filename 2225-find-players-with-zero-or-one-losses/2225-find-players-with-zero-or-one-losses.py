class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loserCount = {}
        winners = set()
        
        for w, l in matches:
            loserCount[l] = 1 + loserCount.get(l, 0)
            winners.add(w)
        
        zeroLoss = []
        
        oneLoss = []
        
        for w in winners:
            if w not in loserCount.keys():
                zeroLoss.append(w)
        
        for l, c in loserCount.items():
            if c == 1:
                oneLoss.append(l)
        
        return [sorted(zeroLoss), sorted(oneLoss)]