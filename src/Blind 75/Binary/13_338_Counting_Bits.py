def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    arr = [0]
    if n == 0:
        return arr
    else:
        for i in range(1,n+1):
            if i & (i-1) == 0:
                arr.append(1)
            else:
                if i%2 == 0:
                    arr.append(arr[i/2])
                else:
                    arr.append(arr[i//2]+1)
        return arr