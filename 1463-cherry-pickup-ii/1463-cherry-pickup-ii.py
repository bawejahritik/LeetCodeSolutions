class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        cache = {}
        
        def dfs(currRow, roboA, roboB):
            if roboA < 0 or roboA>=COLS or roboB < 0 or roboB >= COLS:
                return 0
            if currRow == ROWS:
                return 0
            if (currRow, roboA, roboB) in cache:
                return cache[(currRow, roboA, roboB)]
            currResult = grid[currRow][roboA] + grid[currRow][roboB]
            
            currMax = 0
            for x in range(roboA-1, roboA+2):
                for y in range(roboB-1, roboB+2):
                    if x < y:
                        currMax = max(currMax, dfs(currRow+1, x, y))
            
            currResult += currMax
            cache[(currRow, roboA, roboB)] = currResult
            return currResult
        
        return dfs(0, 0, COLS-1)