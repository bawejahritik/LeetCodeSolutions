class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = [0]
        visited = set()
        
        def bfs(x, y):
            q = deque([(x, y)]) 
            visited.add((x, y))
            while len(q) > 0:
                x, y = q.popleft()
                sides = 4
                for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= i < len(grid) and 0<=j<len(grid[0]):
                        if grid[i][j] == 1:
                            sides -= 1
                        if (i, j)  not in visited:
                            q.append((i, j))
                            visited.add((i, j))
                if grid[x][y] == 1:
                    perimeter[0] += sides
        
        bfs(0, 0)
        return perimeter[0]