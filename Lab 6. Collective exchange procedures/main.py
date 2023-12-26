from mpi4py import MPI


def f(x):
    return x


def integrate(a, b, n):
    if n <= 0:
        return "Error: n must be a positive integer or not the same as a size of processes"
    if b <= a:
        return "Error: b must be greater than a"
    h = (b - a) / n
    res = 0.5 * (f(a) + f(b)) * h
    x = a
    for i in range(1, n):
        x += h
        res += f(x) * h
    return res


if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    if rank == 0:
        a = float(input("Input a: "))
        b = float(input("Input b: "))
        n = int(input("Input n: "))
    else:
        a = None
        b = None
        n = None
    a = comm.bcast(a, root=0)
    b = comm.bcast(b, root=0)
    n = comm.bcast(n, root=0)
    comm.barrier()
    wtime = MPI.Wtime()
    len_ = (b - a) / size
    local_n = n // size
    local_a = a + rank * len_
    local_b = local_a + len_
    local_res = integrate(local_a, local_b, local_n)
    result = comm.reduce(local_res, op=MPI.SUM, root=0)
    comm.barrier()
    wtime = MPI.Wtime() - wtime
    if rank == 0:
        print(f"Integral from {a} to {b} = {result}")
        print(f"Working time: {wtime} seconds")
