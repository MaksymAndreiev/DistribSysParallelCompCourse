import time

import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


class FoxAlgorithm:
    def __init__(self, A, B, n_proc):
        self.A = A
        self.B = B
        self.n_proc = n_proc

    def find_nearest_divider(self, s, p):
        i = s
        while i > 1:
            if p % i == 0:
                break
            if i >= s:
                i += 1
            else:
                i -= 1
            if i > np.sqrt(p):
                i = min(s, p // s) - 1
        return i if i >= s else p // i if i != 0 else p

    def multiply(self):
        if not (self.A.shape[0] == self.A.shape[1] and self.B.shape[0] == self.B.shape[1] and self.A.shape[0] ==
                self.B.shape[0]):
            raise Exception("Matrix A and B have different dimensions!")

        n_proc = min(self.n_proc, self.A.shape[0])
        n_proc = self.find_nearest_divider(n_proc, self.A.shape[0])
        step = self.A.shape[0] // n_proc

        if rank == 0:
            # Initialize matrices
            A = np.random.rand(self.A.shape[0], self.A.shape[1])
            B = np.random.rand(self.B.shape[0], self.B.shape[1])
            C = np.zeros((self.A.shape[0], self.B.shape[1]))

            # Scatter A and B matrices to other processes
            for i in range(1, n_proc):
                A_block = A[i * step:(i + 1) * step, :]
                B_block = np.copy(B)
                comm.Send(A_block, dest=i, tag=11)
                comm.Send(B_block, dest=i, tag=12)
        else:
            # Receive A and B matrices from process 0
            A_block = np.empty((step, self.A.shape[1]))
            B_block = np.empty((self.B.shape[0], self.B.shape[1]))
            comm.Recv(A_block, source=0, tag=11)
            comm.Recv(B_block, source=0, tag=12)

        # Initialize block result matrix
        block_res = np.zeros((step, self.B.shape[1]))

        # Multiply blocks
        for i in range(step):
            for j in range(self.B.shape[1]):
                for k in range(self.A.shape[1]):
                    block_res[i, j] += A_block[i, k] * B_block[k, j]

        # Gather block results to process 0
        if rank == 0:
            C_block = block_res
            for i in range(1, n_proc):
                C_block_part = np.empty((step, self.B.shape[1]))
                comm.Recv(C_block_part, source=i, tag=13)
                C_block = np.vstack((C_block, C_block_part))
            for i in range(self.A.shape[0]):
                for j in range(self.B.shape[1]):
                    for k in range(n_proc):
                        C[i, j] += C_block[i // step * n_proc + k, j]
        else:
            comm.Send(block_res, dest=0, tag=13)

        return C


if rank == 0:
    # Initialize matrices
    A = np.random.rand(20, 20)
    B = np.random.rand(20, 20)
else:
    A = None
    B = None

# Broadcast A and B matrices to all processes
A = comm.bcast(A, root=0)
B = comm.bcast(B, root=0)

# Initialize FoxAlgorithm object and perform matrix multiplication
fox_algorithm = FoxAlgorithm(A, B, n_proc=4)
start_time = time.time()

C = fox_algorithm.multiply()

end_time = time.time()

if rank == 0:
    print(C)
    print("Execution time: {:.5f} seconds".format(end_time - start_time))
