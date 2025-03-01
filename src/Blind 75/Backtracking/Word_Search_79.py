def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    visited = set()
    found = [False]

    def dfs(curr_word, start):
        if found[0]:
            return
        
        row, col = start[0], start[1]
        word_index = len(curr_word)

        # if out of bounds or start is visited already, return nothing
        if row < 0 or row >= ROWS or col < 0 or col >= COLS or start in visited:
            return

        # Check if current letter matches expected letter
        if board[row][col] != word[word_index]:
            return

        curr_word += board[row][col]
        visited.add(start)
        
        if curr_word == word:
            found[0] = True
            return

        dfs(curr_word, (row + 1, col))  # down  
        dfs(curr_word, (row - 1, col))  # up
        dfs(curr_word, (row, col + 1))  # right
        dfs(curr_word, (row, col - 1))  # left

        curr_word = curr_word[:-1]
        visited.remove(start)
        


    for r in range(ROWS):
        for c in range(COLS):
            dfs("", (r, c))
            if found[0]:
                return True


    return False

board=[["A","B","C","D"],["S","A","A","T"],["A","C","A","E"]]
word="CAT"
print(exist(board, word))