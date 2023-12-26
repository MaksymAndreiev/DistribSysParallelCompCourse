from mpi4py import MPI

# Ініціалізація MPI
comm = MPI.COMM_WORLD  # створюємо комунікатор
myrank = comm.Get_rank()  # отримання рангу процесу
size = comm.Get_size()  # отримуємо кількість процесів
message = myrank  # ініціалізуємо змінну повідомлення рангом процесу
TAG = 0  # встановлюємо тег повідомлення

# Якщо номер поточного процесу парний:
if myrank % 2 == 0:
    # Якщо наступний за поточним процесом не є останнім в комунікаторі:
    if myrank + 1 != size:
        comm.send(message, dest=myrank + 1, tag=TAG)  # відправляємо повідомлення наступному процесу
else:
    # Якщо поточний процес не є першим в комунікаторі:
    if myrank != 0:
        message = comm.recv(source=myrank - 1, tag=TAG)  # отримуємо повідомлення від попереднього процесу
        print(f"received: {message}")  # виводимо отримане повідомлення на екран

# Завершення MPI
MPI.Finalize()

# mpiexec -n 14 python mpi_two_process_message_exchange.py
