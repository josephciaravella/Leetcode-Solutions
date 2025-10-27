def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    curr_wall = "t"
    t,b,l,r = 0,n,0,n
    mtx = [[0 for _ in range(n)] for _ in range(n)]
    x,y = 0,0
    for i in range(n**2):
        
        if curr_wall == "t":
            mtx[y][x] = i+1
            x += 1
            if x == r:
                x -= 1
                y += 1
                t += 1
                curr_wall = "r"

        elif curr_wall == "r":
            mtx[y][x] = i+1
            y += 1
            if y == b:
                y -= 1
                x -= 1
                r -= 1
                curr_wall = "b"

        elif curr_wall == "b":
            mtx[y][x] = i+1
            x -= 1
            if x < l:
                x += 1
                y -= 1
                b -= 1
                curr_wall = "l"


        elif curr_wall == "l":
            mtx[y][x] = i+1
            y -= 1
            if y < t:
                y += 1
                x += 1
                l += 1
                curr_wall = "t"

    return mtx


print(generateMatrix(3))