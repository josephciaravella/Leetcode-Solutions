def rotate(matrix):
    size = int(len(matrix))
    for i in range(int(size/2)):
        matrix[i], matrix[size-1-i] = matrix[size-1-i], matrix[i]
    
    for i in range(size):
        for j in range(i, size):
            if i == j:
                continue
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]