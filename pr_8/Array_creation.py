import numpy as np


def array_creation():

    print("\nSelect the type of array to create:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")

    choice = int(input("Enter your choice: "))

    # ---------------- 1D ARRAY ----------------
    if choice == 1:

        n = int(input("Enter the number of elements: "))

        elements = list(map(int, input(
            f"Enter {n} elements separated by space: "
        ).split()))

        arr = np.array(elements)

        print("\nArray created successfully:")
        print(arr)

        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")

        op = int(input("Enter your choice: "))

        if op == 1:
            index = int(input("Enter index: "))
            print("Element:", arr[index])

        elif op == 2:
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced Array:", arr[start:end])

    # ---------------- 2D ARRAY ----------------
    elif choice == 2:

        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))

        total = rows * columns

        elements = list(map(int, input(
            f"Enter {total} elements separated by space: "
        ).split()))

        arr = np.array(elements).reshape(rows, columns)

        print("\nArray created successfully:")
        print(arr)

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
            print("Enter row range and column range.")

            row_start = int(input("Row start: "))
            row_end = int(input("Row end: "))

            column_start = int(input("Column start: "))
            column_end = int(input("Column end: "))

            print("\nSliced Array:")
            print(arr[row_start:row_end, column_start:column_end])

    # ---------------- 3D ARRAY ----------------
    elif choice == 3:

        depth = int(input("Enter depth: "))
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))

        total = depth * rows * columns

        elements = list(map(int, input(
            f"Enter {total} elements separated by space: "
        ).split()))

        arr = np.array(elements).reshape(depth, rows, columns)

        print("\n3D Array created successfully:")
        print(arr)

        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")

        op = int(input("Enter your choice: "))

        if op == 1:
            depth_index = int(input("Enter depth index: "))
            row = int(input("Enter row index: "))
            column = int(input("Enter column index: "))

            print("Element:", arr[depth_index, row, column])

        elif op == 2:
            print("Enter slicing ranges.")

            depth_start = int(input("Depth start: "))
            depth_end = int(input("Depth end: "))

            row_start = int(input("Row start: "))
            row_end = int(input("Row end: "))

            column_start = int(input("Column start: "))
            column_end = int(input("Column end: "))

            print("\nSliced Array:")
            print(arr[
                depth_start:depth_end,
                row_start:row_end,
                column_start:column_end
            ])

    else:
        print("Invalid choice.")

        return None

    return arr