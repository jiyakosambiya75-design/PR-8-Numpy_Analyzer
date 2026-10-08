import numpy as np


def search_sort_filter(arr):

    print("\nChoose an option:")
    print("1. Search a value")
    print("2. Sort the array")
    print("3. Filter values")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        value = int(input("Enter value to search: "))

        if value in arr:
            print("Value found in the array.")
        else:
            print("Value not found.")

    elif choice == 2:

        print("\nOriginal Array:")
        print(arr)

        sorted_array = np.sort(arr, axis=-1)

        print("\nSorted Array:")
        print(sorted_array)
        print("(Sorting applied row-wise.)")

    elif choice == 3:

        value = int(input("Enter minimum value for filtering: "))

        filtered = arr[arr >= value]

        print("\nFiltered values:")
        print(filtered)

    else:
        print("Invalid choice.")