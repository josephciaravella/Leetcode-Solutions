def exist(board, word: str) -> bool:
    found = False

    def backtrack(path, curr):
        nonlocal found
        y, x = curr
        
        if path == word:
            found = True
            return
        
        if found:
            return

        if y + 1 < len(board) and board[y+1][x] == word[len(path)]:
            temp = board[y][x]
            board[y][x] = "#"
            backtrack(path + board[y+1][x], (y+1,x))
            board[y][x] = temp 

        if y - 1 >= 0 and board[y-1][x] == word[len(path)]:
            temp = board[y][x]
            board[y][x] = "#"
            backtrack(path + board[y-1][x], (y-1,x))
            board[y][x] = temp  

        if x + 1 < len(board[y]) and board[y][x+1] == word[len(path)]:
            temp = board[y][x]
            board[y][x] = "#"
            backtrack(path + board[y][x+1], (y,x+1)) 
            board[y][x] = temp 

        if x - 1 >= 0 and board[y][x-1] == word[len(path)]:
            temp = board[y][x]
            board[y][x] = "#"
            backtrack(path + board[y][x-1], (y,x-1))
            board[y][x] = temp 

        


    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0]:
                backtrack(board[i][j], (i, j))
            if found:
                return True

    return False