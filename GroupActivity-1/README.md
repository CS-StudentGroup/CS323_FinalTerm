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
<!-- Enter reflection here -->

#### Aldrick Gicole
<!-- Enter reflection here -->

#### James Dominic Tion
<!-- Enter reflection here -->

#### Kurt Andre Olaer
As the developer responsible for generating the standardized testing datasets and reviewing the integration pipeline across our algorithms, I observed first-hand that parallelization is not a universal performance solution. While our large workload testing (1,000,000 elements) demonstrated that dividing data across processes provides scaling benefits for CPU-intensive tasks like sorting, it also highlighted massive architectural overhead. For simple tasks like linear search, the OS-level cost of spawning `multiprocessing.Process` instances and serializing data chunks via Inter-Process Communication (IPC) drastically outweighed the extremely low computational cost of basic O(N) traversal. We learned empirically that parallelism essentially introduces synchronization and partitioning latency. It is only practically beneficial when the underlying algorithm's computational density is heavy enough to absorb and justify that communication overhead, which is why scaling sequential approaches is sometimes the superior architectural choice for smaller or simpler workloads.
