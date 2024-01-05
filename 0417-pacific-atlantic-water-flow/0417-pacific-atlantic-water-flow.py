class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        
        def get_neighbors(coord):
            r, c = coord
            neighbors = []
            
            delta_row, delta_col = [1, 0, -1, 0], [0, 1, 0, -1]
            
            for i in range(len(delta_row)):
                nr = r + delta_row[i]
                nc = c + delta_col[i]
                
                if 0<=nr<ROWS and 0<=nc<COLS:
                    neighbors.append((nr, nc))
            
            return neighbors
        
        
        water = [False, False]
        
        def bfs(coord):
            q = collections.deque([coord])
            visited = set()
            visited.add(coord) 
            
            cr, cc = coord
            
            if (cr == 0 or cc == 0): 
                # print("in pacific")
                water[0] = True
                    
            if(cr == ROWS-1 or cc == COLS-1):
                water[1] = True
            
            while len(q) > 0:
                curr = q.popleft()
                # print(curr)
                for neighbor in get_neighbors(curr):
                    r, c = neighbor
                    if neighbor in visited or heights[r][c]>heights[curr[0]][curr[1]]:
                        continue

                    if (r == 0 or c == 0): 
                        # print("in pacific")
                        water[0] = True
                    
                    if(r == ROWS-1 or c == COLS-1):
                        water[1] = True

                    q.append(neighbor)
                    visited.add(neighbor)
                 
            # print(curr, water)
            if water[0] and water[1]:
                res.append([coord[0], coord[1]])
                # print("in", coord[0], coord[1])
            
            water[0] = False
            water[1] = False
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i==0 or j==0) and (i==ROWS-1 or j==COLS-1):
                    # print("out", i, j)
                    res.append([i, j])
                    continue
                bfs((i, j))
        
        
        
#         print(heights[0][97], heights[0][98], heights[0][99])
        
#         bfs((0, 98))
        return res
                    
                    
                