### **Homework 4**: Parallel Programming

#### **4.1 Comparing Execution Time: Threads vs. Processes**

- **Task**:
  1. Implement a function to compute Fibonacci numbers.
  2. Compare execution time for large numbers `n` under the following scenarios:
     - Synchronous execution.
     - Execution using 10 threads (`threading`).
     - Execution using 10 processes (`multiprocessing`).
  3. For each scenario, execute the function 10 times in parallel and measure the total execution time.
- **Constraint**:
  - `concurrent.futures` is not allowed. The task focuses on manual management of threads and processes.
- **Artifact**: A text file with execution time measurements for each method.

---

#### **4.2 Parallelizing Numerical Integration**

- **Task**:
  1. Rewrite the numerical integration function:
     ```python
     import math
     def integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
         acc = 0
         step = (b - a) / n_iter
         for i in range(n_iter):
             acc += f(a + i * step) * step
         return acc
     ```
  2. Add support for parallel execution using:
     - `ThreadPoolExecutor`
     - `ProcessPoolExecutor`
  3. Include logging to indicate the start and completion of each task.
  4. Measure execution time for `integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)` with varying numbers of jobs (`n_jobs` from 1 to `cpu_num * 2`).
- **Artifacts**:
  - A log file with execution details.
  - A table comparing execution times for both methods (`ThreadPoolExecutor` and `ProcessPoolExecutor`) depending on the number of threads/processes.

---

#### **4.3 Interprocess Communication**

- **Task**:
  1. Implement an application with interprocess communication:
     - The main process sends strings through `stdin` to process `A`.
     - Process `A` stores the strings in a queue, converts them to lowercase (`.lower()`), and forwards them to process `B`.
     - Process `B` encodes the strings using `rot13`, prints the result to `stdout`, and sends the result back to the main process via a queue.
  2. Process `A` sends messages to `B` with a delay of 5 seconds.
  3. Use `multiprocessing.Queue` (and optionally `multiprocessing.Pipe` and threads for data handling).
- **Artifact**: A text file documenting the program's interaction with the user, including timestamps for the messages.
