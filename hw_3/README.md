### **Homework 3**: Matrix Library

The goal of this assignment is to implement a library for matrix operations, including basic arithmetic, optimization, and caching.

---

#### **3.1 Basic Matrix Operations**

- Create a matrix class implementing the following operations via operator overloading:
  - Addition (`+`)
  - Multiplication (element-wise `*` and matrix `@`)
- Handle exceptions:
  - Raise a `ValueError` if matrix dimensions do not match.
- Steps:
  1. Generate two `10x10` matrices using `np.random.randint(0, 10, (10, 10))` (set seed=0 for reproducibility).
  2. Perform three operations (`+`, `*`, `@`) and save the results to files:
     - `matrix+.txt`
     - `matrix*.txt`
     - `matrix@.txt`
- **Artifact**: Three text files containing the results of the operations.

---

#### **3.2 Advanced Features with Mixins**

- Create a matrix class with the following features using mixins:
  - Implement all standard arithmetic operations (using NumPy).
  - Add via mixins:
    - The ability to save objects to a file.
    - A user-friendly string representation of the matrix (`__str__`).
    - Getters and setters for class fields.
- Minimize the number of methods defined directly in the classes.
- **Artifact**: Text files as in Task 3.1.

---

#### **3.3 Hash Function and Caching**

- Extend the matrix class:
  - Implement the `__hash__` method:
    - The hash function should be unique and based on the matrix data.
    - Provide a brief textual description of the hash function in the code comments.
  - Implement caching for matrix multiplication results using the hash function.
- Find hash collisions:
  - Create four matrices (`A.txt`, `B.txt`, `C.txt`, `D.txt`) such that:
    - `hash(A) == hash(C)` and `A != C`
    - `B == D` and `A @ B != C @ D`
  - Save the results of matrix multiplications:
    - `A @ B` in `AB.txt`
    - `C @ D` in `CD.txt`
  - Save the matrix hashes in `hash.txt`.

- **Artifact**: Seven files:
  - `A.txt`, `B.txt`, `C.txt`, `D.txt` — matrices.
  - `AB.txt`, `CD.txt` — multiplication results.
  - `hash.txt` — hashes of matrices `AB` and `CD`.
