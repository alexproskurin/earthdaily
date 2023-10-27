import numpy as np

def matrix_pow(matrix, exponent):
    if exponent == 1:
        return matrix
    if exponent % 2 == 0:
        half_pow = matrix_pow(matrix, exponent // 2)
        return np.dot(half_pow, half_pow)
    else:
        return np.dot(matrix, matrix_pow(matrix, exponent - 1))

def fibonacci(n):
    if n <= 1:
        return n
    # matrix that defined recursive relationship
    recur_matrix = np.array([[1, 1], [1, 0]])
    # the following is computed in O(log n) by taking advantage of 
    # exponent arithmetic
    sol = matrix_pow(recur_matrix, n - 1)
    return sol[0, 0]
