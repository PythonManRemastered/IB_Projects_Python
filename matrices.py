def add_matrices():
    matrix1 = [[1,2,3],
               [4,5,6]]
    matrix2 = [[2,3,4],
               [5,6,7]]
    matrix3 = [[0,0,0],
               [0,0,0]]
    for i in range(0, 2):
        for j in range(0,3):
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
    print(matrix3)


def transpose():
    matrix = [[1,2,3], 
              [4,1,8]]
    matrix_transposed = [[0,0], [0,0], [0,0]]

    for i in range(0,3):
        for j in range(0,2):
            matrix_transposed[i][j] = matrix[j][i]
    print(matrix_transposed)


def self_m():
    matrix1 = [[1, 2, 3],
               [4, 5, 6]]
    matrix2 = [[7, 8],
               [9, 10],
               [11, 12]]
    product_matrix = [[0 for i in range(len(matrix1))] for i in range(len(matrix2[0]))]
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix2[0])):
            sum = 0 
            for k in range(0, len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            product_matrix[i][j] = sum
    print(product_matrix)
      
self_m()