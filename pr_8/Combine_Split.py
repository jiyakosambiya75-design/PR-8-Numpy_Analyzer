import numpy as np


def combine_split(arr):

    print("\nChoose an option:")
    print("1. Combine Arrays")
    print("2. Split Array")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        elements = list(map(int, input(
            f"Enter the elements of another array to combine ({arr.size} elements separated by space): "
        ).split()))

        arr2 = np.array(elements).reshape(arr.shape)

        print("\nOriginal Array:")
        print(arr)

        print("\nSecond Array:")
        print(arr2)

        combined = np.vstack((arr, arr2))

        print("\nCombined Array (Vertical Stack):")
        print(combined)

    elif choice == 2:

        print("\nOriginal Array:")
        print(arr)

        if arr.shape[0] >= 2:
            split_array = np.array_split(arr, 2)

            print("\nSplit Arrays:")
            for part in split_array:
                print(part)
        else:
            print("Array cannot be split.")

    else:
        print("Invalid choice.")