import numpy as np
import time


def cannon_method(matrix_a, matrix_b, block_size):
    matrix_size = len(matrix_a)
    num_of_blocks = matrix_size // block_size
    result_matrix = np.zeros((matrix_size, matrix_size), dtype=np.int32)

    for i in range(num_of_blocks):
        for j in range(num_of_blocks):
            for k in range(num_of_blocks):
                block_a = matrix_a[i * block_size:(i + 1) * block_size,
                          (j + k) % num_of_blocks * block_size:((j + k) % num_of_blocks + 1) * block_size]
                block_b = matrix_b[(i + k) % num_of_blocks * block_size:((i + k) % num_of_blocks + 1) * block_size,
                          j * block_size:(j + 1) * block_size]
                result_matrix[i * block_size:(i + 1) * block_size, j * block_size:(j + 1) * block_size] += np.dot(
                    block_a, block_b)

    return result_matrix


matrix_size = 100
block_size = 4

matrix_a = np.random.randint(0, 10, (matrix_size, matrix_size))
matrix_b = np.random.randint(0, 10, (matrix_size, matrix_size))

start_time = time.time()

result_matrix = cannon_method(matrix_a, matrix_b, block_size)

end_time = time.time()

print(result_matrix)
print("Час виконання: {:.5f} секунд".format(end_time - start_time))
