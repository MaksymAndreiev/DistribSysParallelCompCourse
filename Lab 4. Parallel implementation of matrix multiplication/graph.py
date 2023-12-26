import matplotlib.pyplot as plt

# Дані для 7 процесів
n = [100, 200, 400, 800]
p_4 = 4
T1 = [0.019246, 0.357236, 2.682453, 24.109888]
Tp_4 = [0.01854, 0.08751, 0.712354, 7.165489]


# Дані для 13 процесів
p_8 = 8
Tp_8 = [0.0186685, 0.224743, 0.425568, 3.973127]

# Розрахунок Sp
Sp_4 = []
for i in range(len(n)):
    Sp_4.append(T1[i] / Tp_4[i])

print('Sp:', Sp_4)

# Розрахунок Ep
Ep_4 = []
for i in range(len(n)):
    Ep_4.append(Sp_4[i] / p_4)

print('Ep:', Ep_4)


# Розрахунок Ep
Ep_8 = []
for i in range(len(n)):
    Ep_8.append(T1[i] / (p_8 * Tp_8[i]))

print(Ep_8)

# Розрахунок Sp
Sp_8 = []
for i in range(len(n)):
    Sp_8.append(T1[i] / Tp_8[i])

print('Sp:', Sp_8)

# Побудова графіків
plt.figure(figsize=(12, 10))

# Графік T1
plt.subplot(1, 2, 1)

# Графік Sp
plt.subplot(1, 2, 1)
plt.plot(n, Sp_4, 'bo-', label='4 процесa')
plt.plot(n, Sp_8, 'ro-', label='8 процесів')
plt.title('Sp')
plt.xlabel('n')
plt.ylabel('S')
plt.legend()

# Графік Ep
plt.subplot(1, 2, 2)
plt.plot(n, Ep_4, 'bo-', label='4 процесa')
plt.plot(n, Ep_8, 'ro-', label='8 процесів')
plt.title('Ep')
plt.xlabel('n')
plt.ylabel('E')
plt.legend()

plt.show()
