class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans1 = ans2 = ans3 = True
        
        def checkRow(i):
            temp = []
            for j in range(0, 9):
                if board[i][j] != ".":
                    temp.append(int(board[i][j]))
            return len(set(temp)) == len(temp)
        
        def checkCol(j):
            temp = []
            for i in range(0, 9):
                if board[i][j] != ".":
                    temp.append(int(board[i][j]))
            return len(set(temp)) == len(temp)
        
        def checkBox(row, col):
            temp = []
            
            for i in range(0, 3):
                for j in range(0, 3):
                     if board[row+i][col+j] != ".":
                            temp.append(int(board[row+i][col+j]))
            
            return len(set(temp)) == len(temp)
        
        for i in range(0, 9):
            ans1 = ans1 and checkRow(i)
            
        for j in range(0, 9):
            ans2 = ans2 and checkCol(j)
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                ans3 = ans3 and checkBox(i, j)

        return ans1 and ans2 and ans3