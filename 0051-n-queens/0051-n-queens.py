class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pD = set()
        nD = set()
        
        board = [["."]*n for i in range(n)]
        
        res = []
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in pD or (r-c) in nD:
                    continue
                
                col.add(c)
                pD.add(r+c)
                nD.add(r-c)
                board[r][c] = "Q"
                
                backtrack(r+1)
                
                col.remove(c)
                pD.remove(r+c)
                nD.remove(r-c)
                board[r][c] = "."
            
        backtrack(0)
        return res