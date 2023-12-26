from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

Ar_size = 12
Ac_size = 12
Bc_size = 12

if rank == 0:
    A = np.random.randint(10, size=(Ar_size, Ac_size))
    B = np.random.randint(10, size=(Ac_size, Bc_size))
else:
    A = None
    B = None

A = comm.bcast(A, root=0)
B = comm.bcast(B, root=0)
C = np.zeros((Ar_size, Bc_size), dtype=int)

proc_part_A = Ar_size // size
part_A = proc_part_A * Ac_size
proc_part_B = Bc_size // size
part_B = proc_part_B * Ac_size

buf_A = np.empty(part_A, dtype=int)
buf_B = np.empty(part_B, dtype=int)
buf_C = np.empty(proc_part_A * Bc_size, dtype=int)

start_time = time.time()

comm.Scatter(A.reshape(-1), buf_A, root=0)
comm.Scatter(B.reshape(-1), buf_B, root=0)

for i in range(proc_part_A):
    for j in range(Bc_size):
        tmp = 0
        for k in range(Ac_size):
            tmp += buf_A[i * Ac_size + k] * B[k, j]
        buf_C[i * Bc_size + j] = tmp

comm.Gather(buf_C, C.reshape(-1), root=0)

end_time = time.time()

if rank == 0:
    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)
    print("Matrix C:")
    print(C)
    print("Time: {:.5f} sec".format(end_time - start_time))
