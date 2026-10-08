NumPy Analyzer 🔢

NumPy Analyzer is a Python-based console application that demonstrates different NumPy operations using an object-oriented approach.

This project allows users to create 1D, 2D, and 3D NumPy arrays and perform mathematical operations, combining, splitting, searching, sorting, filtering, and statistical calculations.

---

📌 Features

- Create 1D, 2D, and 3D NumPy arrays
- Perform mathematical operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Combine and split arrays
- Search values in an array
- Sort array elements
- Filter values based on a condition
- Calculate statistical values:
  - Sum
  - Mean
  - Median
  - Standard Deviation
  - Variance
- Menu-driven console interface
- Object-Oriented Programming using a Python class

---

🛠️ Technologies Used

- Python
- NumPy
- Object-Oriented Programming (OOP)

---

📂 Project Structure

NumPyAnalyzer/
│
├── main.py
└── README.md

---

⚙️ Installation

1. Install Python

Make sure Python is installed on your computer.

Check the Python version:

python --version

2. Install NumPy

Open the terminal and run:

pip install numpy

---

▶️ How to Run

Run the Python file using:

python main.py

The program will display the following menu:

Welcome to the NumPy Analyzer!
========================================
1. Create a NumPy Array
2. Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter
5. Aggregates and Statistics
6. Exit

---

🔢 1. Create a NumPy Array

The user can create three types of arrays:

1. 1D Array
2. 2D Array
3. 3D Array

Example: 1D Array

Enter your choice: 1
Enter elements: 10 20 30 40 50

Array created successfully:
[10 20 30 40 50]

Example: 2D Array

Enter your choice: 2
Enter rows: 2
Enter columns: 3
Enter elements: 10 20 30 40 50 60

Array created successfully:
[[10 20 30]
 [40 50 60]]

Example: 3D Array

Enter your choice: 3
Enter layers: 2
Enter rows: 2
Enter columns: 2
Enter elements: 1 2 3 4 5 6 7 8

Array created successfully:
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]

---

➕ 2. Mathematical Operations

The application supports:

1. Addition
2. Subtraction
3. Multiplication
4. Division

Example:

First Array:
[10 20 30]

Second Array:
[1 2 3]

Addition result:

[11 22 33]

---

🔗 3. Combine or Split Arrays

Combine Arrays

Two arrays can be combined using NumPy's "vstack()" function.

Example:

Array 1:
[1 2 3]

Array 2:
[4 5 6]

Combined result:

[[1 2 3]
 [4 5 6]]

Split Array

An array can also be divided into multiple parts using NumPy's "split()" function.

---

🔍 4. Search, Sort, and Filter

Search

The program checks whether a particular value exists in the array.

Enter value: 20
Value found.

Sort

The array can be sorted using:

np.sort(self.array)

Filter

Values greater than a given number can be displayed.

Example:

Array:
[10 20 30 40 50]

Enter value: 25

Filtered values:
[30 40 50]

---

📊 5. Aggregates and Statistics

The project provides the following statistical operations:

1. Sum
2. Mean
3. Median
4. Standard Deviation
5. Variance

Example:

Array:
[10 20 30 40 50]

Output:

Sum: 150
Mean: 30.0
Median: 30.0

These operations use NumPy functions such as:

np.sum()
np.mean()
np.median()
np.std()
np.var()

---

🧠 OOP Concept Used

The project uses a class named:

class NumPyAnalyzer:

An object is created using:

obj = NumPyAnalyzer()

The class contains different methods for different operations:

create_array()
mathematical_operations()
combine_split()
search_sort_filter()
statistics()

The current array is stored using:

self.array

---

🎯 Learning Objectives

Through this project, I practiced:

- NumPy arrays
- 1D, 2D, and 3D arrays
- Array reshaping
- Mathematical operations
- Array combining and splitting
- Searching and sorting
- Boolean filtering
- Statistical functions
- Python classes and objects
- Menu-driven programs

---

🚀 Future Improvements

Some possible improvements for this project are:

- Add maximum and minimum operations
- Add array indexing and slicing
- Add random array generation
- Add file saving and loading
- Add better error handling
- Add matrix operations
- Add a graphical user interface

---

Explanation video:
https://drive.google.com/file/d/1IbFmgP16m1nXw20CFGBdi5GKT7ydmOaV/view?usp=drivesdk

---

🤝 Let's Connect I'd love to connect with fellow learners, developers, and Python enthusiasts! 💙

💼 LinkedIn 🔗 http://www.linkedin.com/in/jiya-kosambiya-86306141b

📧 Email ✉️ jiyakosambiya75@gmail.com
---

👩‍💻 Author

Jiya Kosmbiya

B.Sc. IT with AI & ML Specialization

---

⭐ Conclusion

NumPy Analyzer is a simple console-based project created to understand and practice NumPy and Object-Oriented Programming in Python.

It combines multiple NumPy concepts into one interactive application and helps build a strong foundation for further learning in Data Science, Machine Learning, and AI.
