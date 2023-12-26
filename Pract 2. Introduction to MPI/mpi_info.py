from mpi4py import MPI

# Ініціалізація MPI
comm = MPI.COMM_WORLD  # створюємо комунікатор
myrank = comm.Get_rank()  # отримання рангу процесу
numprocs = comm.Get_size()  # отримання кількості процесів

# виводимо інформацію про ранг та кількість процесів
print("Process {} of {}".format(myrank, numprocs))

MPI.Finalize()

# mpiexec -n 4 python mpi_info.py
