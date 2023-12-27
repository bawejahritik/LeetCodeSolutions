from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        visited = set()
        
        def bfs(coord):
            r, c = coord
            q = deque([coord])
            visited.add((r, c))
            while len(q) > 0:
                
                curr = q.popleft()
                cr, cc = curr
                coordinates = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
                for dr, dc in coordinates:
                    nr = cr + dr
                    nc = cc + dc
                    
                    if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        visited.add((nr, nc))
                                
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs((i, j))
                    res += 1
        
        
        return res           