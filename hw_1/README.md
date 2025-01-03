### **Homework 1**: CLI Applications

The task involves implementing several CLI applications. In addition to the code, you must provide a text file with examples of commands and their outputs from the terminal to demonstrate functionality.

---

#### **1.1 Implementation of the `nl` Utility**

Create a simplified version of the `nl` utility with the following features:

- Outputs numbered lines from a file to `stdout`.
- If no file is specified, reads lines from `stdin`.
- Should behave similarly to the `nl -b a` command.

---

#### **1.2 Implementation of the `tail` Utility**

Create a simplified version of the `tail` utility with the following features:

- Outputs the last 10 lines from each specified file.
- If more than one file is provided, the utility should display the file name before processing each file.
- If no files are specified, outputs the last 17 lines from `stdin`.
- The output format should match the behavior of the original `tail` utility.

---

#### **1.3 Implementation of the `wc` Utility**

Create a utility that works similarly to `wc` without additional options. The program should:

- Output statistics for each file as three numbers (line count, word count, and byte count) followed by the file name.
- If multiple files are provided, display a summary (`total`) at the end.
- If no files are specified, read data from `stdin` and output statistics without a file name.

---
