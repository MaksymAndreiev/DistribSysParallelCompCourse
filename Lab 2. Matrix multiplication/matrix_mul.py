import time
import numpy as np


def multiply(matrix_a, matrix_b):
    # Отримуємо розмірність матриць
    n = matrix_a.shape[0]
    m = matrix_b.shape[1]
    p = matrix_a.shape[1]

    # Перевірка, що матриці можна помножити
    if p != matrix_b.shape[0]:
        print("Матриці неможливо помножити")
        return None

    # Створюємо пусту матрицю для результату
    result_matrix = np.zeros((n, m))

    # Послідовний цикл для множення матриць
    start_time = time.time()
    for i in range(n):
        for j in range(m):
            for k in range(p):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    end_time = time.time()

    execution_time = end_time - start_time
    print("Час виконання множення: ", execution_time, "секунд")

    return result_matrix


a = np.random.rand(500, 500)
b = np.random.rand(500, 500)

c = multiply(a, b)
print(c)
