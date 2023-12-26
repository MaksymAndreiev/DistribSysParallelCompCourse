# PRACTICE 2. Introduction to the development of parallel programs using MPI

**TASKS TO COMPLETE**

1. In the source text of the C++ program, the following calls are missing procedures for connecting to MPI, determining
   the number of processes and the rank of the process. Add these calls, compile and run the program.
   ```
   #include "mpi.h"
   #include <stdio.h>
   int main(int argc,char *argv[])
   {
      int myid, numprocs;
      fprintf(stdout,&quot;Process %d %d\n&quot;, myid, numprocs);
      MPI_Finalize();
      return 0;
   }
   ```
2. In the source text of the C++ program, the calls to the of the procedures of the standard blocking two-point
   exchange. It is assumed that when two processes start, one of them sends a message to the other. Add these calls,
   compile and run the program.
   ```   
   #include "mpi.h"
   #include <stdio.h>
   int main(int argc,char *argv[])
   {
      int myid, numprocs;
      char message[20];
      int myrank; MPI_Status status;
      int TAG = 0; MPI_Init(&amp;argc &amp;argv);
      MPI_Comm_rank(MPI_COMM_WORLD &amp;myrank);
      if (myrank == 0)
      {
         strcpy(message, &quot;Hi, Second Processor!&quot;);
         MPI_Send(...);
      }
      else
      {
         MPI_Recv(...);
         printf(&quot;received: %s\n&quot;, message);
      }
      MPI_Finalize();
      return 0;
   }
   ```
3. In the source text of the C++ program, the calls to the procedures of the standard blocking two-point exchange. It is
   assumed that when an even number of processes are started, those that have an even rank, send messages to the next
   highest rank processes. Add these calls, compile and run the program.
   ```
   #include &quot;mpi.h&quot;
   #include &lt;stdio.h&gt;
   int main(int argc,char *argv[])
   {
      int myrank, size, message;
      int TAG = 0;
      MPI_Status status; MPI_Init(&amp;argc &amp;argv);
      MPI_Comm_rank(MPI_COMM_WORLD &amp;myrank);
      MPI_Comm_size(MPI_COMM_WORLD &amp;size);
      message = myrank;
      if((myrank % 2) == 0)
      {
         if((myrank + 1) != size) MPI_Send(...);
      }
      else
      {
         if(myrank != 0)
         MPI_Recv(...);
         printf(&quot;received :%i\n&quot;, message);
      }
      MPI_Finalize();
      return 0;
   }
   ```

# ПРАКТИЧНЕ ЗАНЯТТЯ 2. Введення в розробку паралельних програм з використанням MPI

**ЗАВДАННЯ ДЛЯ ВИКОНАННЯ**

1. У початковому тексті програми на мові C++ пропущені виклики
   процедур підключення до MPI, визначення кількості процесів і рангу
   процесу. Додати ці виклики, відкомпілювати і запустити програму.

   ```
   #include "mpi.h"
   #include <stdio.h>
   int main(int argc,char *argv[])
   {
      int myid, numprocs;
      fprintf(stdout,&quot;Process %d %d\n&quot;, myid, numprocs);
      MPI_Finalize();
      return 0;
   }
   ```

2. У початковому тексті програми на мові C++ пропущені виклики
   процедур стандартного блокуючого двоточкового обміну.
   Передбачається, що при запуску двох процесів один з них відправляє
   повідомлення іншому. Додати ці виклики, відкомпілювати і запустити
   програму.
   ```   
   #include "mpi.h"
   #include <stdio.h>
   int main(int argc,char *argv[])
   {
      int myid, numprocs;
      char message[20];
      int myrank; MPI_Status status;
      int TAG = 0; MPI_Init(&amp;argc &amp;argv);
      MPI_Comm_rank(MPI_COMM_WORLD &amp;myrank);
      if (myrank == 0)
      {
         strcpy(message, &quot;Hi, Second Processor!&quot;);
         MPI_Send(...);
      }
      else
      {
         MPI_Recv(...);
         printf(&quot;received: %s\n&quot;, message);
      }
      MPI_Finalize();
      return 0;
   }
   ```

3. У початковому тексті програми на мові C++ пропущені виклики
   процедур стандартного блокуючого двохточкового обміну.
   Передбачається, що при запуску парного числа процесів, ті з них, які
   мають парний ранг, відправляють повідомлення наступним по величині
   рангу процесам. Додати ці виклики, відкомпілювати і запустити програму.
   ```
   #include &quot;mpi.h&quot;
   #include &lt;stdio.h&gt;
   int main(int argc,char *argv[])
   {
      int myrank, size, message;
      int TAG = 0;
      MPI_Status status; MPI_Init(&amp;argc &amp;argv);
      MPI_Comm_rank(MPI_COMM_WORLD &amp;myrank);
      MPI_Comm_size(MPI_COMM_WORLD &amp;size);
      message = myrank;
      if((myrank % 2) == 0)
      {
         if((myrank + 1) != size) MPI_Send(...);
      }
      else
      {
         if(myrank != 0)
         MPI_Recv(...);
         printf(&quot;received :%i\n&quot;, message);
      }
      MPI_Finalize();
      return 0;
   }
   ```