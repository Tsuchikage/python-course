### **Homework 2**: LaTeX Generator

The goal of this assignment is to implement a LaTeX generator in a functional programming style. **Using third-party libraries for LaTeX generation is prohibited**.

---

#### **2.1 Table Generation**

- Implement a function for generating tables in `.tex` format:
  - The function should take a nested list (list of lists) as input.
  - The output should be a string containing valid LaTeX table code.
- Verify the correctness of the generated code, e.g., using **Overleaf**.
- Save an example of the function's usage to a `.tex` file:
  - Use a separate module (.py file) that imports the function.
  - Artifact: a `.tex` file demonstrating the function's output.

> **Tip:** If you haven’t worked with LaTeX before, this is an excellent opportunity to start!

---

#### **2.2 Image Generation**

- Extend the previous module with a function for generating LaTeX code to include images:
  - Use any `.png` file as the image.
- Prepare a library:
  - Build the library using **setuptools** or **conda-build**.
  - Publish the library to a repository (e.g., **PyPI** or **Anaconda**).
  - Install the library and use it to generate:
    - A PDF file containing a table (from Task 2.1) and an embedded image.
- Artifacts:
  - The generated PDF file.
  - A link to the library's repository.

> **Note:** Use `pdflatex` to generate the PDF. Make sure to install a LaTeX distribution.

---

#### **2.3 Automation with Docker**

- Automate the build process:
  - Create a **Dockerfile** that installs all required dependencies.
  - Inside the container:
    - Run your code to generate a `.tex` file.
    - Generate a PDF file.
- Artifact:
  - The Dockerfile, saved in the `hw02` folder.

> **Optional:** Using **docker-compose** is allowed for convenience.
