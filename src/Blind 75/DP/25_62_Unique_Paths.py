def uniquePaths(m, n):
    tab = [1] * (m*n)
    # instead of a 2D array with rows and cols, flatten it and iterate thru with + n
    for i in range(1,m*n):
        if (i-n) < 0 or i % n == 0:
            continue
        else:
            tab[i] = tab[i-n] + tab[i-1]

    return tab[-1]

print(uniquePaths(3,7))