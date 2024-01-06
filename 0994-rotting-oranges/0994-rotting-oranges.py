class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        def checkgrid():
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 1:
                        return False
            return True
        
        if checkgrid():
            return 0
        
        q = collections.deque([])
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        res = -1
        
        while q:
            
            res += 1
            count = len(q)
                        
            delta_r = [1, 0, -1, 0]
            delta_c = [0, 1, 0, -1]
            
            for _ in range(count):
                curr = q.popleft()
                r, c = curr

                for i in range(4):
                    nr, nc = r + delta_r[i], c + delta_c[i]

                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                
        return res if checkgrid() else -1
                    