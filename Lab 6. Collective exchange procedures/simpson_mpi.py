import math

from mpi4py import MPI


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


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

a = 0.0
b = -2.0
time = 0.0
local_a = 0.0
local_b = 0.0
len_ = 0.0
local_n = 0
local_res = 0.0
result = 0.0

if rank == 0:
    n = int(input("Enter n: "))
    for i in range(1, size):
        comm.send(n, dest=i)
else:
    n = comm.recv(source=0)

a = comm.bcast(a, root=0)
b = comm.bcast(b, root=0)

comm.barrier()

time = MPI.Wtime()
len_ = (b - a) / size

local_n = n // size
local_a = a + rank * len_
local_b = local_a + len_
local_res = simpson(local_a, local_b, local_n)
result = comm.reduce(local_res, op=MPI.SUM, root=0)
comm.barrier()
time = MPI.Wtime() - time

if rank == 0:
    print(f"Integral from {a} to {b} = {result}")
    print(f"Working time: {time} seconds")

MPI.Finalize()
