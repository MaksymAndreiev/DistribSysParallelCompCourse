import random
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Змінна, що відстежує чи відбувалось перестановлення елементів
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Перестановка елементів
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Якщо жодного перестановлення не було, то масив відсортований і можна зупинити цикл
        if not swapped:
            break
    return arr


# Генеруємо масив з випадковими числами
arr = [random.randint(1, 10000) for i in range(10000)]

# Вимірюємо час виконання сортування
start_time = time.time()
sorted_arr = bubble_sort(arr)
end_time = time.time()

# Виводимо відсортований масив і час виконання сортування
print("Sorted array:", sorted_arr)
print("Time taken:", end_time - start_time, "seconds")
