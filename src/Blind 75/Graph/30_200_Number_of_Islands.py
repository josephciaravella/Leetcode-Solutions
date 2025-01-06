def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    from collections import deque
    visited = set()
    islands = 0

    graph = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                if i > 0 and grid[i-1][j] == '1':
                    graph[i][j].append((i-1, j))
                if j > 0 and grid[i][j-1] == '1':
                    graph[i][j].append((i, j-1))
                if i < len(grid) - 1 and grid[i+1][j] == '1':
                    graph[i][j].append((i+1, j))
                if j < len(grid[0]) - 1 and grid[i][j+1] == '1':
                    graph[i][j].append((i, j+1))

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            touched = False
            # singular island with no neighbours
            if grid[row][col] == '1' and not graph[row][col]:
                islands += 1
                continue

            # ocean or visited
            if grid[row][col] == '0' or grid[row][col] in visited:
                continue
            
            queue = deque([(row, col)]) 
            while queue:
                r, c = queue.popleft() #tuple
                coord = (r, c)

                if coord in visited:
                    continue

                visited.add(coord)

                for node in graph[r][c]:
                    if node not in visited and node:
                        queue.append(node)
                        touched = True
            
            if touched:
                islands += 1
    
    return islands

print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])) # 1
print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])) # 3
    