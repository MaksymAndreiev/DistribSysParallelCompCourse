import re
import subprocess
import matplotlib.pyplot as plt
import numpy as np


# розміри векторів для обчислення скалярного добутку
vector_sizes = np.arange(10, 100001, 10000).tolist()

# кількість процесів для паралельного обчислення
num_procs = np.arange(2, 18, 1).tolist()

# збереження часів виконання
speedups = []
efficiencies = []

# обчислення прискорення та ефективності виконання послідовних та паралельних обчислень
for vector_size in vector_sizes:
    cmd = f"mpiexec -n 5 python scalar_product.py {vector_size}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    output = result.stdout
    regex = r"Speedup: (\d+\.\d+)\nEfficiency: (\d+\.\d+)"
    matches = re.findall(regex, output)

    speedup = float(matches[0][0])
    efficiency = float(matches[0][1])
    speedups.append(speedup)
    efficiencies.append(efficiency)

# будування графіків
plt.figure(figsize=(10, 5))

# графік прискорення
plt.subplot(2, 2, 1)
plt.plot(vector_sizes, speedups, '-o')
plt.xlabel('Vector Size')
plt.ylabel('Speedup')
plt.title('Speedup vs Vector Size')

# графік ефективності
plt.subplot(2, 2, 2)
plt.plot(vector_sizes, efficiencies, '-o')
plt.xlabel('Vector Size')
plt.ylabel('Efficiency')
plt.title('Efficiency vs Vector Size')

speedups = []
efficiencies = []

# обчислення прискорення та ефективності виконання послідовних та паралельних обчислень
for num in num_procs:
    cmd = f"mpiexec -n {num} python scalar_product.py 10000"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    output = result.stdout
    regex = r"Speedup: (\d+\.\d+)\nEfficiency: (\d+\.\d+)"
    matches = re.findall(regex, output)

    speedup = float(matches[0][0])
    efficiency = float(matches[0][1])
    speedups.append(speedup)
    efficiencies.append(efficiency)


# графік прискорення
plt.subplot(2, 2, 3)
plt.plot(num_procs, speedups, '-o')
plt.xlabel('Number of Processes')
plt.ylabel('Speedup')
plt.title('Speedup vs Number of Processes')

# графік ефективності
plt.subplot(2, 2, 4)
plt.plot(num_procs, efficiencies, '-o')
plt.xlabel('Number of Processes')
plt.ylabel('Efficiency')
plt.title('Efficiency vs Number of Processes')

plt.suptitle('Speedup and Efficiency of scalar product')

#===================================================================

# розміри векторів для обчислення скалярного добутку
vector_sizes = np.arange(10, 8001, 1000).tolist()

# кількість процесів для паралельного обчислення
num_procs = np.arange(2, 18, 1).tolist()

# збереження часів виконання
speedups = []
efficiencies = []

# обчислення прискорення та ефективності виконання послідовних та паралельних обчислень
for vector_size in vector_sizes:
    cmd = f"mpiexec -n 5 python max_element.py {vector_size}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    output = result.stdout
    regex = r"Speedup: (\d+\.\d+)\nEfficiency: (\d+\.\d+)"
    matches = re.findall(regex, output)

    speedup = float(matches[0][0])
    efficiency = float(matches[0][1])
    speedups.append(speedup)
    efficiencies.append(efficiency)

# будування графіків
plt.figure(figsize=(10, 5))

# графік прискорення
plt.subplot(2, 2, 1)
plt.plot(vector_sizes, speedups, '-o')
plt.xlabel('Vector Size')
plt.ylabel('Speedup')
plt.title('Speedup vs Vector Size')

# графік ефективності
plt.subplot(2, 2, 2)
plt.plot(vector_sizes, efficiencies, '-o')
plt.xlabel('Vector Size')
plt.ylabel('Efficiency')
plt.title('Efficiency vs Vector Size')

speedups = []
efficiencies = []

# обчислення прискорення та ефективності виконання послідовних та паралельних обчислень
for num in num_procs:
    cmd = f"mpiexec -n {num} python max_element.py 1000"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    output = result.stdout
    regex = r"Speedup: (\d+\.\d+)\nEfficiency: (\d+\.\d+)"
    matches = re.findall(regex, output)

    speedup = float(matches[0][0])
    efficiency = float(matches[0][1])
    speedups.append(speedup)
    efficiencies.append(efficiency)


# графік прискорення
plt.subplot(2, 2, 3)
plt.plot(num_procs, speedups, '-o')
plt.xlabel('Number of Processes')
plt.ylabel('Speedup')
plt.title('Speedup vs Number of Processes')

# графік ефективності
plt.subplot(2, 2, 4)
plt.plot(num_procs, efficiencies, '-o')
plt.xlabel('Number of Processes')
plt.ylabel('Efficiency')
plt.title('Efficiency vs Number of Processes')

plt.suptitle('Speedup and Efficiency of min max')


plt.tight_layout()
plt.show()

