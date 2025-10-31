def validRow(row) -> bool:
    nums = set([])
    for val in row:
        if val != ".":
            if val not in nums:
                nums.add(val)
            else:
                return False
    return True
            
def validRows(board) -> bool:
    for i in range(9):
        row = board[i]
        if not validRow(row):
            return False
    return True

def validColumns(board) -> bool:
    for i in range(9):
        arr = []
        for j in range(9):
            arr.append(board[j][i])
        if not validRow(arr):
            return False
    return True

def validBox(board) -> bool:
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            arr = []
            for i in range(3):
                for j in range(3):
                    arr.append(board[box_row + i][box_col + j])
            if not validRow(arr):
                return False
    return True

def isValidSudoku(board) -> bool:
    return validRows(board) and validColumns(board) and validBox(board)

board1 = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

isValidSudoku(board1)