import time

import numpy as np
from mpi4py import MPI


def scalar_product(vector_size):
    # Ініціалізація MPI та отримання загальної кількості процесів та рангу поточного процесу
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    sequential_time = 0
    parallel_time = 0

    start_time = time.time()
    if rank == 0:
        # Господарський процес
        print("Master process started")

        # Ініціалізація векторів
        vector_a = np.random.randint(low=1, high=10, size=vector_size)
        vector_b = np.random.randint(low=1, high=10, size=vector_size)

        if size > vector_size:
            print(f"Reducing size from {size} to {vector_size}")
            size = vector_size

        # Розбиття векторів на частини та розсилка їх до підлеглих процесів
        for i in range(1, size):
            if i == size - 1 and vector_size % (size - 1) != 0:
                start = (i - 1) * (vector_size // (size - 1))
                end = start + (vector_size // (size - 1)) + (vector_size % (size - 1))
            else:
                start = (i - 1) * (vector_size // (size - 1))
                end = start + (vector_size // (size - 1))
            comm.send(vector_a[start:end], dest=i, tag=1)
            comm.send(vector_b[start:end], dest=i, tag=2)

    else:
        # Підлеглий процес
        print("Slave process started")
        myrank = comm.Get_rank()  # отримання рангу процесу
        print("Process {} of {}".format(myrank + 1, size))

        # Отримання векторів від майстер-процесу
        local_vector_a = comm.recv(source=0, tag=1)
        local_vector_b = comm.recv(source=0, tag=2)

        local_vector_size = local_vector_a.size

        # Обчислення локальної суми
        local_sum = 0
        for i in range(local_vector_size):
            local_sum += local_vector_a[i] * local_vector_b[i]

        print('Local sum:')
        print(local_sum)
        # Відправка локальної суми до майстер-процесу
        comm.send(local_sum, dest=0)

    if rank == 0:
        # Ініціалізація глобальної суми та лічильника отриманих сум
        global_sum = 0
        received_sums = 0

        # Отримання локальних сум від усіх підлеглих процесів
        for i in range(1, size):
            local_sum = comm.recv(source=i)
            global_sum += local_sum
            received_sums += 1

        parallel_time = time.time() - start_time
        print("Scalar product is:", global_sum)

        # Обчислення послідовного скалярного добутку для порівняння з паралельним
        start_time_s = time.time()
        sequential_sum = 0
        for i in range(vector_size):
            sequential_sum += vector_a[i] * vector_b[i]
        sequential_time = time.time() - start_time_s
        # Вивід результатів
        print("Sequential time:", sequential_time)
        print("Parallel time:", parallel_time)
        if parallel_time > 0:
            print("Speedup:", sequential_time / parallel_time)
            print("Efficiency:", (sequential_time / (size * parallel_time)))

    MPI.Finalize()

    return sequential_time, parallel_time


if __name__ == "__main__":
    # отримання розміру вектору з аргументів командного рядка
    import sys

    if len(sys.argv) != 2:
        print("Usage: mpiexec -n <num_procs> python scalar_product.py <vector_size>")
        sys.exit(1)
    vector_size = int(sys.argv[1])

    # виклик функції min_max з переданим розміром вектору
    scalar_product(vector_size)

# mpiexec -n 5 python scalar_product.py
