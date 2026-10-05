import numpy as np


def array_creation():

    print("\nSelect the type of array to create:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        n = int(input("Enter the number of elements: "))
        elements = list(map(int, input("Enter elements separated by space: ").split()))

        arr = np.array(elements)

        print("\nArray created successfully:")
        print(arr)

    elif choice == 2:

        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))

        elements = list(map(int, input(f"Enter {rows * columns} elements for the array separated by space: ").split()))

        arr = np.array(elements).reshape(rows, columns)

        print("\nArray created successfully:")
        print(arr)

    while True:
        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")

        op = int(input("Enter your choice: "))

        if op == 1:
            row = int(input("Enter row index: "))
            column = int(input("Enter column index: "))
            print("Element:", arr[row, column])

        elif op == 2:

            row_range = input("Enter the row range (start:end): ")
            column_range = input("Enter the column range (start:end): ")

            r1, r2 = map(int, row_range.split(":"))
            c1, c2 = map(int, column_range.split(":"))

            print("\nSliced Array:")
            print(arr[r1:r2, c1:c2])

        elif choice == 3:

            depth = int(input("Enter depth: "))
            rows = int(input("Enter rows: "))
            columns = int(input("Enter columns: "))

            total = depth * rows * columns

            elements = list(map(int, input(f"Enter {total} elements separated by space:" ).split()))

            arr = np.array(elements).reshape(depth, rows, columns)

            print("\n3D Array created successfully:")
            print(arr)

        else:
            print("Invalid choice.")

