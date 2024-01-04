class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        def get_neighbors(coord):
            r, c = coord
            
            neighbors = []
            
            delta_row = [1, 0, -1, 0]
            delta_col = [0, 1, 0, -1]
            
            for i in range(len(delta_row)):
                nr = r + delta_row[i]
                nc = c + delta_col[i]
                
                if (0 <= nr < ROWS and 0 <= nc < COLS):
                    neighbors.append((nr, nc))
            
            return neighbors
        
        def bfs(coord):
            q = collections.deque([coord])
            
            while len(q) > 0:
                curr = q.popleft()
                r, c = curr
                
                for neighbor in get_neighbors(curr):
                    nr, nc = neighbor
                    if grid[nr][nc] == "0":
                        continue
                    
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
        
        res = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    bfs((i, j))
                    res += 1
        
        return res