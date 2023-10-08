class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(row: int) -> bool:
            temp = []
            for i in range(0, 9):
                if board[row][i] != ".":
                    temp.append(int(board[row][i]))
            return len(set(temp)) == len(temp)
            
        
        def checkCol(col: int) -> bool:
            temp = []
            for i in range(0, 9):
                if board[i][col] != ".":
                    temp.append(int(board[i][col]))
            return len(set(temp)) == len(temp)
        
        def checkSquare(row: int, col: int) -> bool:
            temp = []
            for i in range(0, 3):
                for j in range(0, 3):
                    if board[row+i][col+j] != ".":
                        temp.append(int(board[row+i][col+j]))
            return len(set(temp)) == len(temp)
        
        ans1, ans2, ans3 = True, True, True
        
        for row in range(0, 9):
            ans1 = ans1 and checkRow(row)
        for col in range(0, 9):
            ans2 = ans2 and checkCol(col)
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                ans3 = ans3 and checkSquare(row, col)
                    
        
        return ans1 and ans2 and ans3