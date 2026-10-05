import numpy as np


def mathematical_operations(arr):

    print("\nChoose a mathematical operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Dot Product")
    print("6. Matrix Multiplication")

    choice = int(input("Enter your choice: "))

    if choice in [1, 2, 3, 4]:

        elements = list(map(int, input(
            f"Enter the same-size array elements ({arr.size} elements separated by space): "
        ).split()))

        arr2 = np.array(elements).reshape(arr.shape)

        print("\nOriginal Array:")
        print(arr)

        print("\nSecond Array:")
        print(arr2)

        if choice == 1:
            result = arr + arr2
            print("\nResult of Addition:")
            print(result)

        elif choice == 2:
            result = arr - arr2
            print("\nResult of Subtraction:")
            print(result)

        elif choice == 3:
            result = arr * arr2
            print("\nResult of Multiplication:")
            print(result)

        elif choice == 4:
            result = arr / arr2
            print("\nResult of Division:")
            print(result)

    elif choice == 5:

        print("\nDot Product:")
        print(np.dot(arr, arr))

    elif choice == 6:

        if arr.ndim == 2:
            print("\nMatrix Multiplication:")
            print(np.matmul(arr, arr))
        else:
            print("Matrix multiplication is available for 2D arrays only.")

    else:
        print("Invalid choice.")