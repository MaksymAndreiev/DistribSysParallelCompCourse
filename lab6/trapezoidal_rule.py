import math
import time


def f(x):
    return (pow(x, 2) + 5 * x + 6) * math.cos(2 * x)


def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    res = 0
    x = a + h
    for i in range(1, n):
        res += f(x)
        x += h
    return (h / 2) * (f(a) + f(b) + 2 * res)


a = 0
b = -2
n = int(input("Enter n: "))

start_time = time.time()
integral = trapezoidal_rule(a, b, n)
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Integral from {a} to {b} = {integral}")
print(f"Working time: {elapsed_time} seconds")
