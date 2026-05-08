Reflection Answers

1. The orders were distributed using a round-robin strategy. The master process created a list of worker chunks and assigned each one based on
chunks[i % workers].append(order). This divides the work evenly across each worker by cycling through the available worker ranks one at a time


2. If there are more orders than workers, each worker receives multiple orders. Because of the round-robin distribution, the workload is spread as evenly as possible among all workers. Some workers may receive one extra order if the number of orders is not perfectly divisible by the number of workers.


3. Each worker was simulated to have processing time using the python random and time module. This randomly delay caused some workers to finish earlier or later than others. This demonstrated how processing speed differences affect total completion time in parallel systmes.


4. Implementing shared memory with multiprocessing and MPI was challenging on the Windows system because MPI and shared memory support did not work reliably in our environment. Due to these compatibility issues, we improvised by avoiding direct shared memory usage and instead used MPI message passing with
comm.send() and comm.recv(), The master process initialized the orders list and distributed copies of the data to each worker process. Every worker processed its assigned orders locally and then sent the completed results back to the master process. This approach avoided shared memory conflicts and worked more consistently on Windows.


5. Since shared memory was not used in this program, simultaneous write conflicts did not occur. Each worker maintained its own local processed list and only communicated completed results back to the master process using MPI communication methods.
If shared memory had been used, race conditions or inconsistent data could occur when multiple workers attempt to write at the same time without synchronization mechanisms like locks or barriers.


6. Consistency was ensured by using MPI’s structured communication model:

- The master process handled order generation and final collection.
- Each worker processed only its assigned orders independently.
- Results were sent back to the master using comm.send() and collected using comm.recv().

Because workers did not directly modify shared data, conflicts were avoided and the final completed order list remained consistent.