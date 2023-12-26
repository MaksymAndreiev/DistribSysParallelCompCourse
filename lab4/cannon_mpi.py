import time

import numpy as np
from mpi4py import MPI


def InitializeMatrix(size, value):
    return np.full((size, size), value, dtype=int)


def Repack(matrix, matrixSize, blockSize):
    matrixBlocks = []
    for i in range(0, matrixSize, blockSize):
        for j in range(0, matrixSize, blockSize):
            matrixBlocks.append(matrix[i:i + blockSize, j:j + blockSize])
    return matrixBlocks


def MultMatrix(left, right, size):
    result = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i, j] += left[i, k] * right[k, j]
    return result.flatten()


# Initialize MPI environment
comm = MPI.COMM_WORLD
myRank = comm.Get_rank()
processorsCount = comm.Get_size()
status = MPI.Status()

# Define blockSize and matrixSize
blockSize = 2
matrixSize = blockSize * processorsCount

# Define matrices
Cb = InitializeMatrix(blockSize, 0)
Ab = InitializeMatrix(blockSize, 0)
Bb = InitializeMatrix(blockSize, 0)

start_time = time.time()

D = InitializeMatrix(matrixSize, 0)
C = InitializeMatrix(matrixSize, 0)
A = InitializeMatrix(matrixSize, 1)
B = InitializeMatrix(matrixSize, 2)

if myRank == 0:
    """
    print("Matrix size:", matrixSize)
    print("Processor count:", processorsCount)
    """
    D = InitializeMatrix(matrixSize, 0)
    C = InitializeMatrix(matrixSize, 0)
    A = InitializeMatrix(matrixSize, 1)
    B = InitializeMatrix(matrixSize, 2)

    startwtime = MPI.Wtime()

    A = Repack(A, matrixSize, blockSize)
    B = Repack(B, matrixSize, blockSize)

comm.barrier()

Ab = np.empty((blockSize, blockSize), dtype=int)
Bb = np.empty((blockSize, blockSize), dtype=int)
comm.Scatter(A, Ab, root=0)
comm.Scatter(B, Bb, root=0)

rowIndex = myRank // processorsCount
columnIndex = myRank % processorsCount

if rowIndex != 0:
    if columnIndex < rowIndex:
        comm.Bsend(Ab.tolist(), dest=myRank + processorsCount - rowIndex, tag=0)
    else:
        comm.Bsend(Ab.tolist(), dest=myRank - rowIndex, tag=0)

if columnIndex != 0:
    if rowIndex < columnIndex:
        comm.Bsend(Bb.tolist(), dest=myRank + (processorsCount - columnIndex) * processorsCount, tag=1)
    else:
        comm.Bsend(Bb.tolist(), dest=myRank - processorsCount * columnIndex, tag=1)

if rowIndex != 0 and columnIndex != 0:
    buf = np.empty((blockSize, blockSize), dtype=int)
    comm.Recv(buf, source=MPI.ANY_SOURCE, tag=0, status=status)
    Ab = np.array(buf)
    buf = np.empty((blockSize, blockSize), dtype=int)
    comm.Recv(buf, source=MPI.ANY_SOURCE, tag=1, status=status)
    Bb = np.array(buf)

if rowIndex == 0 and columnIndex != 0:
    buf = np.empty((blockSize, blockSize), dtype=int)
    comm.Recv(buf, source=MPI.ANY_SOURCE, tag=1, status=status)
    Bb = np.array(buf)

if rowIndex != 0 and columnIndex == 0:
    buf = np.empty((blockSize, blockSize), dtype=int)
    comm.Recv(buf, source=MPI.ANY_SOURCE, tag=0, status=status)
    Ab = np.array(buf)

comm.Barrier()
Cb = MultMatrix(Ab, Bb, blockSize)

for i in range(processorsCount - 1):
    if myRank == rowIndex * processorsCount:
        comm.Bsend(Ab.tolist(), dest=(rowIndex + 1) * processorsCount - 1, tag=0)
    else:
        comm.Bsend(Ab.tolist(), dest=myRank - 1, tag=0)

    if myRank < processorsCount:
        comm.Bsend(Bb.tolist(), dest=myRank + (processorsCount - 1) * processorsCount, tag=1)
    else:
        comm.Bsend(Bb.tolist(), dest=myRank - processorsCount, tag=1)

    buf = np.empty((blockSize, blockSize), dtype=int)
    comm.Recv(buf, source=MPI.ANY_SOURCE, tag=0, status=status)
    Ab = np.array(buf)

    buf = np.empty((blockSize, blockSize), dtype=int)
    comm.Recv(buf, source=MPI.ANY_SOURCE, tag=1, status=status)
    Bb = np.array(buf)

    Cb = MultMatrix(Ab, Bb, blockSize)

end_time = time.time()

if myRank == 0:
    print(C)
    print("Execution time: {:.5f} seconds".format(end_time - start_time))
