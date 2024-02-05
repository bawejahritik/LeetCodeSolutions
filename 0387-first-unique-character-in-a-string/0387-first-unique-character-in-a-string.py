class Solution:
    def firstUniqChar(self, s: str) -> int:
        frq = {}
        q = deque()
        
        for i, c in enumerate(s):
            frq[c] = 1 + frq.get(c, 0)
            q.append((i, c))
        
        while q:
            i, c = q.popleft()
            if frq[c] == 1:
                return i
        
        return -1