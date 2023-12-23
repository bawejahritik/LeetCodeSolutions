class Solution:
    def isPathCrossing(self, path: str) -> bool:
        res = [0, 0]
        visited = set()
        
        visited.add((0, 0))
        
        for p in path:
            if p == 'N':
                res[0] += 1
            elif p == 'S':
                res[0] -= 1
            elif p == 'E':
                res[1] += 1
            else:
                res[1] -= 1
            
            # print(res)
            temp = (res[0], res[1])
            if temp not in visited:
                visited.add(temp)
            else:
                return True
        
        return False