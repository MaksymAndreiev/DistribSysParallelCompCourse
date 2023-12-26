import time

import numpy as np


def gauss_elimination(A, b):
    n = len(A)

    for i in range(n):
        max_idx = abs(A[i:, i]).argmax() + i
        if A[max_idx, i] == 0:
            raise ValueError("Matrix is singular.")
        A[[i, max_idx]] = A[[max_idx, i]]
        b[[i, max_idx]] = b[[max_idx, i]]
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    x = np.zeros_like(b)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.sum(A[i, i + 1:] * x[i + 1:])) / A[i, i]

    return x


np.random.seed(0)
n = 100
A = np.random.rand(n, n)
b = np.random.rand(n)

start_time = time.time()
x = gauss_elimination(A.copy(), b.copy())
end_time = time.time()

print("Sequential time:", end_time - start_time)
print("Solution:", x)
