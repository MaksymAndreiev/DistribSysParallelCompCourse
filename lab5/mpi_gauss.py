import numpy as np
from mpi4py import MPI


def parallel_gauss_elimination(A, b, comm):
    rank = comm.Get_rank()
    size = comm.Get_size()
    n = len(A)

    for i in range(n):
        pivot_row = i + abs(A[i:, i]).argmax()
        if rank == 0:
            if A[pivot_row, i] == 0:
                raise ValueError("Matrix is singular.")
            A[[i, pivot_row]] = A[[pivot_row, i]]
            b[[i, pivot_row]] = b[[pivot_row, i]]

        pivot_value = np.array([A[i, i]])
        comm.Bcast(pivot_value, root=0)
        comm.Bcast(A[i, :], root=0)
        comm.Bcast(np.array([b[i]]), root=0)

        for j in range(i + 1 + rank, n, size):
            factor = A[j, i] / pivot_value[0]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

        if rank != 0:
            for k in range(i + 1, n):
                comm.Bcast(A[k, :], root=0)
                comm.Bcast(np.array([b[k]]), root=0)

    x = np.zeros_like(b)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.sum(A[i, i + 1:] * x[i + 1:])) / A[i, i]

    return x


np.random.seed(0)
n = 100
A = np.random.rand(n, n)
b = np.random.rand(n)

comm = MPI.COMM_WORLD
start_time = MPI.Wtime()
x = parallel_gauss_elimination(A.copy(), b.copy(), comm)
end_time = MPI.Wtime()

if comm.Get_rank() == 0:
    print("Parallel time:", end_time - start_time)
    print("Solution:", x)
