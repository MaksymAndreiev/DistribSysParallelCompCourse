import random
import time


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in arr[1:]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [pivot] + quick_sort(right)


# Генеруємо масив з випадковими числами
arr = [random.randint(1, 10000) for i in range(10000)]

# Вимірюємо час виконання сортування
start_time = time.time()
sorted_arr = quick_sort(arr)
end_time = time.time()

# Виводимо відсортований масив і час виконання сортування
print("Sorted array:", sorted_arr)
print("Time taken:", end_time - start_time, "seconds")
