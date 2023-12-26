import matplotlib.pyplot as plt

# Дані для 7 процесів
n = [100, 200, 400, 800, 1000]
p_4 = 4
T1 = [0.016011953353881836, 0.06300592422485352, 0.2590060234069824, 1.2121813297271729, 2.0300161838531494]
Tp_4 = [0.030912499991245568, 0.04128780000610277, 0.10065989999566227, 0.39646339998580515, 0.6167797000380233]


# Дані для 13 процесів
p_8 = 8
Tp_8 = [0.038300600000013674, 0.05905760000001692, 0.07968010002514347, 0.25298900000052527, 0.3729330999776721]

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
