import math
import time


def f(x):
    return (pow(x, 2) + 5 * x + 6) * math.cos(2 * x)


def simpson(a, b, n):
    h = (b - a) / n
    sum = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            sum += 2 * f(x)
        else:
            sum += 4 * f(x)
    return (h / 3) * sum


# Параметри обчислення
a = 0
b = -2
n = int(input("Enter n: "))

# Обчислення інтегралу
start_time = time.time()
integral = simpson(a, b, n)
elapsed_time = time.time() - start_time

# Вивід результатів та часу виконання
print("Integral from {} to {} = {}".format(a, b, integral))
print("Working time: {} seconds".format(elapsed_time))
