def pacificAtlantic(heights):
    """
    :type heights: List[List[int]]
    :rtype: List[List[int]]
    """

    rows, cols = len(heights), len(heights[0])
    canReachPacific, canReachAtlantic = set(), set()

    def dfs(row, col, canReach, prevHeight):
        stack = [(row, col, prevHeight)]

        while stack:
            r, c, prevHeight = stack.pop()
            coords = (r, c)
            if coords in canReach or r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prevHeight:
                continue
            
            canReach.add((r, c))

            if r-1 >= 0:
                stack.append((r-1, c, heights[r][c]))
            if r+1 < rows:
                stack.append((r+1, c, heights[r][c]))
            if c-1 >= 0:
                stack.append((r, c-1, heights[r][c]))
            if c+1 < cols:
                stack.append((r, c+1, heights[r][c]))


    for col in range(cols):
        dfs(0, col, canReachPacific, heights[0][col])
        dfs(rows-1, col, canReachAtlantic, heights[rows - 1][col])


    for row in range(rows):
        dfs(row, 0, canReachPacific, heights[row][0])
        dfs(row, cols-1, canReachAtlantic, heights[row][cols-1])


    result = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) in canReachPacific and (r, c) in canReachAtlantic:
                result.append([r, c])
    return result


print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]


















#     flowingIn = {}
#     canReachPacific = {}
#     canReachAtlantic = {}
#     # initialize graph
#     for i in range(len(heights)):
#         for j in range(len(heights[0])):
#             flowingIn[(i, j)] = []
#             canReachPacific[(i, j)] = False
#             canReachAtlantic[(i, j)] = False
    
#     # build graph
#     for coord in :
#         if coord[0] > 0 and heights[coord[0]][coord[1]] <= heights[coord[0]-1][coord[1]]:
#             flowingIn[coord].append((coord[0]-1, coord[1]))
        
#         if coord[0] < len(heights)-1 and heights[coord[0]][coord[1]] <= heights[coord[0]+1][coord[1]]:
#             flowingIn[coord].append((coord[0]+1, coord[1]))
        
#         if coord[1] > 0 and heights[coord[0]][coord[1]] <= heights[coord[0]][coord[1]-1]:
#             flowingIn[coord].append((coord[0], coord[1]-1))
        
#         if coord[1] < len(heights[0])-1 and heights[coord[0]][coord[1]] <= heights[coord[0]][coord[1]+1]:
#             flowingIn[coord].append((coord[0], coord[1]+1))


#     def dfsPacific(canReach):
#         # backtracking = True
#         visited = set()
#         for coord in range(len(heights[0])):
#             if canReach == canReachPacific and (coord[0] == 0 or coord[1] == 0):
#                 canReach[coord] = True


#             # elif canReach == canReachAtlantic and (coord[0] == len(heights)-1 or coord[1] == len(heights[0])-1):
#             #     canReach[coord] = True

#             if canReach[coord]:
#                 for neighbour in flowingIn[coord]:
#                     canReach[neighbour] = True
#                 continue
            
#             else:
#                 if coord in visited:
#                     continue

#                 stack = [coord]

#                 while stack:

#                     curr = stack.pop()
                    
#                     if curr not in visited:
#                         visited.add(curr)

#                         for neighbour in flowingIn[curr]:
#                             if canReach[neighbour]:
#                                 canReach[curr] = True
#                                 for neighbour in flowingIn[curr]:
#                                     canReach[neighbour] = True
#                                 break
#                             elif neighbour not in visited:
#                                 stack.append(neighbour)
                        
                        
                        
                        


                

    
    
#     # dfs for pacific
#     dfsPacific(canReachPacific)
    
#     # dfs for atlantic
#     dfs(canReachAtlantic)


#     result = []
#     for i in range(len(heights)):
#         for j in range(len(heights[0])):
#             if canReachPacific[(i, j)] and canReachAtlantic[(i, j)]:
#                 result.append([i, j])
    
#     return result


# print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]