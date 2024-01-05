class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ROWS, COLS = len(board), len(board[0])
        
        def get_neighbors(coord):
            neighbors = []
            r, c = coord
            
            delta_r = [1, 0, -1, 0]
            delta_c = [0, 1, 0, -1]
            
            for i in range(len(delta_r)):
                nr = r + delta_r[i]
                nc = c + delta_c[i]
                
                if (0<=nr<ROWS and 0<=nc<COLS):
                    neighbors.append((nr, nc))
                    
            return neighbors
        
        visited = set()
        
        def bfs(coord):
            q = collections.deque([coord])            
            visited.add(coord)
            currLvl = [coord]
            can = True
            while len(q) > 0:
                curr = q.popleft()

                for neighbor in get_neighbors(curr):
                    r, c = neighbor
                    if board[r][c] == 'X' or neighbor in visited:
                        continue
                    
                    if r == 0 or r == ROWS-1 or c == 0 or c == COLS-1:
                        can = False
                    
                    q.append(neighbor)
                    visited.add(neighbor)
                    currLvl.append(neighbor)
                
                # print(can, currLvl)
                
            if can:
                for i, j in currLvl:
                    board[i][j] = 'X'
        
        for i in range(1, ROWS-1):
            for j in range(1, COLS-1):
                if (i, j) in visited or board[i][j] == 'X':
                    continue
                bfs((i, j))
        
                    
                    
                    
                