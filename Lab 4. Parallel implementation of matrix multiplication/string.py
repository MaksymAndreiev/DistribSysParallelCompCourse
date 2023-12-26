import time

import numpy as np


def standard_matrix_multiplication(A, B):
    A_height, A_width = A.shape
    B_height, B_width = B.shape
    C = np.zeros((A_height, B_width))

    for i in range(A_height):
        for j in range(B_width):
            for k in range(A_width):
                C[i, j] += A[i, k] * B[k, j]

    return C


# Задаємо кількість елементів у матрицях
n = 10

# Генеруємо рандомні матриці з n елементів
A = np.random.randint(low=0, high=10, size=(n, n))
B = np.random.randint(low=0, high=10, size=(n, n))

start_time = time.time()
C = standard_matrix_multiplication(A, B)
end_time = time.time()

print(C)
print("Час виконання: {:.5f} секунд".format(end_time - start_time))
