class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = [0]
        ROWS, COLS = len(grid), len(grid[0])
        
        def get_neighbors(coord):
            r, c = coord
            neighbors = []
            delta_row, delta_col = [1, 0, -1, 0], [0, 1, 0, -1]
            
            for i in range(len(delta_row)):
                nr = r + delta_row[i]
                nc = c + delta_col[i]
                
                if (0<=nr<ROWS and 0<=nc<COLS):
                    neighbors.append((nr, nc))
            
            return neighbors
        
        def bfs(coord):
            # print("isnide")
            q = collections.deque([coord])
            currArea = 0
            r, c = coord
            grid[r][c] = 0
            while len(q) > 0:
                curr = q.popleft()
                currArea += 1
                for neighbor in get_neighbors(curr):
                    nr, nc = neighbor
                    
                    if grid[nr][nc] == 0:
                        continue
                    
                    grid[nr][nc] = 0
                    q.append(neighbor)
                
                # print(currArea)
            
            res[0] = max(res[0], currArea)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    bfs((i, j))
        
        return res[0]
            