import time

import numpy as np
from mpi4py import MPI


def max_val(vector_size):
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
        array = np.random.randint(low=1, high=vector_size + 1, size=vector_size)

        # Розбиття векторів на частини та розсилка їх до підлеглих процесів
        for i in range(1, size):
            if i == size - 1 and vector_size % (size - 1) != 0:
                start = (i - 1) * (vector_size // (size - 1))
                end = start + (vector_size // (size - 1)) + (vector_size % (size - 1))
            else:
                start = (i - 1) * (vector_size // (size - 1))
                end = start + (vector_size // (size - 1))
            comm.send(array[start:end], dest=i, tag=i)

    else:
        # Підлеглий процес
        print("Slave process started")
        myrank = comm.Get_rank()  # отримання рангу процесу
        print("Process {} of {}".format(myrank + 1, size))

        # Отримання масиву від майстер-процесу
        local_array = comm.recv(source=0, tag=myrank)

        local_array_size = local_array.size

        # # Бульбашкове сортування для локального масиву
        # for i in range(local_array_size):
        #     for j in range(local_array_size - i - 1):
        #         if local_array[j] > local_array[j + 1]:
        #             # Міняємо місцями елементи, якщо вони стоять в неправильному порядку
        #             local_array[j], local_array[j + 1] = local_array[j + 1], local_array[j]


        # Знаходимо локальний мінімум та максимум
        # local_max = local_array[local_array_size - 1]
        # або просто максимальний елемент
        local_max = max(local_array)
        print('Local max:')
        print(local_max)

        # Відправка локального максимуму до майстер-процесу
        comm.send(local_max, dest=0)

    if rank == 0:
        # Ініціалізація глобального максимума
        global_max = float('-inf')
        # Отримання локальних мінімумів та максимумів від усіх підлеглих процесів
        for i in range(1, size):
            local_max = comm.recv(source=i)
            if local_max > global_max:
                global_max = local_max

        parallel_time = time.time() - start_time
        # Вивід результатів
        print('Global max:')
        print(global_max)

        start_time_s = time.time()

        # # Функція для послідовного бульбашкового сортування масиву
        # def bubble_sort(arr):
        #     n = len(arr)
        #     # Проходження по елементам масиву
        #     for i in range(n):
        #         # Останні і елементи вже будуть відсортовані, тому вони не беруться до уваги
        #         for j in range(n - i - 1):
        #             # Перевірка, чи наступний елемент менший за поточний
        #             if arr[j] > arr[j + 1]:
        #                 # Якщо так, то міняємо їх місцями
        #                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
        #     return arr
        #
        # sorted_arr = bubble_sort(array)
        # max_value = sorted_arr[-1]

        max_value = max(array)

        sequential_time = time.time() - start_time_s

        # Вивід результатів
        print("Sequential time:", sequential_time)
        print("Parallel time:", parallel_time)
        if parallel_time > 0:
            print("Speedup:", sequential_time / parallel_time)
            print("Efficiency:", (sequential_time / (size * parallel_time)))

    MPI.Finalize()

    return sequential_time, parallel_time

    # отримання розміру вектору з аргументів командного рядка


if __name__ == "__main__":
    # отримання розміру вектору з аргументів командного рядка
    import sys

    if len(sys.argv) != 2:
        print("Usage: mpiexec -n <num_procs> python max_element.py <vector_size>")
        sys.exit(1)
    vector_size = int(sys.argv[1])

    # виклик функції max_val з переданим розміром вектору
    max_val(vector_size)
