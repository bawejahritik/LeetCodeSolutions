class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = [[-1 for _ in range(n)] for _ in range(n)]
        
        cache = {}
        
        for i, j, price in flights:
            graph[i][j] = price
        
        def dfs(curr, k):
            
            if (curr, k) in cache:
                return cache[curr, k]              
            
            if curr == dst:
                return 0
            
            if k < 0:
                return float('inf')
            
            minimum = float('inf')
            for i in range(n):
                if graph[curr][i] != -1:
                    minimum = min(minimum, graph[curr][i] + dfs(i, k-1))
            cache[(curr, k)] = minimum
            return minimum
        
        res = dfs(src, k)
        return res if res != float('inf') else -1