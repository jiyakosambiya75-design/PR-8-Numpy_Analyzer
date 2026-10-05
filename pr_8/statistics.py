import numpy as np


def statistics(arr):

    print("\nChoose an aggregate/statistical operation:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Standard Deviation")
    print("5. Variance")
    print("6. Minimum")
    print("7. Maximum")
    print("8. Percentile")
    print("9. Correlation")

    choice = int(input("Enter your choice: "))

    print("\nOriginal Array:")
    print(arr)

    if choice == 1:
        print("Sum:", np.sum(arr))

    elif choice == 2:
        print("Mean:", np.mean(arr))

    elif choice == 3:
        print("Median:", np.median(arr))

    elif choice == 4:
        print("Standard Deviation:", np.std(arr))

    elif choice == 5:
        print("Variance:", np.var(arr))

    elif choice == 6:
        print("Minimum:", np.min(arr))

    elif choice == 7:
        print("Maximum:", np.max(arr))

    elif choice == 8:
        p = float(input("Enter percentile (0-100): "))
        print("Percentile:", np.percentile(arr, p))

    elif choice == 9:

        elements = list(map(int, input(
            f"Enter {arr.size} elements for second array: "
        ).split()))

        arr2 = np.array(elements).reshape(arr.shape)

        correlation = np.corrcoef(arr.flatten(), arr2.flatten())[0, 1]

        print("Correlation Coefficient:", correlation)

    else:
        print("Invalid choice.")