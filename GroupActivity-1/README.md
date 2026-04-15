# CS323 - Parallel and Distributed Computing

## Group Activity 1: Sequential vs Parallel Algorithms

### Group Members and Contributions

* **Johanie Abulkhair** - Parallel Sorting Algorithm
* **Brandon Ian Gimolatan** - Sequential Sorting Algorithm
* **Aldrick Gicole** - Sequential Searching Algorithm
* **James Dominic Tion** - Parallel Searching Algorithm
* **Kurt Andre Olaer** - Dataset Generation & Code Review

### How to Run

To demonstrate correctness and dynamically evaluate performance execution times against varying dataset loads natively, run `main.py` directly from the active environment. Make sure you are positioned strictly inside the parent folder when executing.

```bash
python main.py
```

Executing this module drops you into a controlled interactive menu environment allowing testing across the `Small` (1,000), `Medium` (100,000), and `Large` (1,000,000) integer constraints requested by the group activity parameters across Random, Sorted, and Reverse Sorted distributions.

---

### Individual Reflections and Analysis

**Please discuss:**

* Differences observed between sequential and parallel execution
* Performance behavior across dataset sizes
* Challenges encountered during implementation
* Insights about overhead, synchronization, or merging
* Situations where parallelism was beneficial or unnecessary

#### Johanie Abulkhair

<!-- Enter reflection here -->

#### Brandon Ian Gimolatan

In this activity, I learned that sequential algorithms execute tasks one at a time, making them simple and efficient for small datasets, while parallel algorithms divide tasks and run them simultaneously, making them faster for larger datasets but more complex due to synchronization and communication. I observed that sequential execution performed better for small inputs, while parallel execution showed improvements as the dataset size increased. One of the main challenges was managing multiple processes and ensuring correct results, especially when merging sorted data and handling search outputs. Overall, I realized that parallel algorithms are not always faster because of overhead, and choosing between sequential and parallel approaches depends on the size and complexity of the problem.

#### Aldrick Gicole

In Todays Activity. I notice that when i Parallel Execution is slower. I test it multiple times and the result is that Even running 
a simple linear search the parallel search is always slower than the sequential search.
i think its because of os overheat and also the data transmission delays take much longer than the search. If its a small arrays 
i think the sequential search is faster but when it comes to intensive task like sorting arrays of 1,000,000 elements the parallel search became faster. 
So Parallelism is usefull when it calculates heavy enough to ignore the delays of the background system.

#### James Dominic Tion

As Observed from testing Sequential beats Parallel in sorting, but as n grows larger Parallel beats Sequential. I was tasked to create the Parallel Search algorithm, my first problem was where to implement the processes, the second is how to divide the labor. To solve the first one was to implement it directly to the search algorithm, second was to split the data into "chunks" so that each process only needs to deal with their chunk. Using multiple process requires a lot of overhead to startup since it has to start up its own python interpreter which will take some time, parallelism though was unnecessary if the dataset is too small.

#### Kurt Andre Olaer

Parallel execution is not always faster. Testing showed that running a simple linear search in parallel was always slower than sequential search because the OS overhead and data transmission delays take much longer than the search itself. However, for mathematically intensive tasks like sorting an array of 1,000,000 elements, parallelism successfully split the heavy workload and became much faster. Basically, parallelism is only useful when the calculation is heavy enough to ignore the background system delays.
