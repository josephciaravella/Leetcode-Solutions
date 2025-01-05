def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    res = [1, 2]
    if (n == 1):
        return 1

    elif (n == 2):
        return 2
    
    i = 2
    while (i < n):
        res.append(res[i-1]+res[i-2])
        i += 1
    return res[n-1]