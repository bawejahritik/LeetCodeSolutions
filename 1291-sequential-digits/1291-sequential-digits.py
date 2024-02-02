class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        
        q = deque(range(1, 10))
        
        while q:
            n = q.popleft()
            if n > high:
                continue
            if low <= n <= high:
                res.append(n)
            
            ones = n % 10
            
            if ones < 9:
                n = n*10 + (ones+1)
                q.append(n)
        
        
        return res
            