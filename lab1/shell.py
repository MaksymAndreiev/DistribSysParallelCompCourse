import random
import time


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


# Генеруємо масив з випадковими числами
arr = [random.randint(1, 10000) for i in range(10000)]

# Вимірюємо час виконання сортування
start_time = time.time()
sorted_arr = shell_sort(arr)
end_time = time.time()

# Виводимо відсортований масив і час виконання сортування
print("Sorted array:", sorted_arr)
print("Time taken:", end_time - start_time, "seconds")
