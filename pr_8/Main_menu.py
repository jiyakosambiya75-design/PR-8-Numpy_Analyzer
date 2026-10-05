from Array_creation import array_creation
from Mathematical import mathematical_operations
from Combine_Split import combine_split
from Search_Sort import search_sort_filter
from statistics import statistics


class DataAnalytics:

    def __init__(self):
        self.arr = None

    def show_menu(self):

        print("\n====================================")
        print("       Welcome to NumPy Analyzer")
        print("====================================")

        while True:

            print("\nChoose an option:")
            print("1. Create a NumPy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:

                self.arr = array_creation()

            elif choice == 2:

                if self.arr is None:
                    print("Please create an array first.")
                else:
                    mathematical_operations(self.arr)

            elif choice == 3:

                if self.arr is None:
                    print("Please create an array first.")
                else:
                    combine_split(self.arr)

            elif choice == 4:

                if self.arr is None:
                    print("Please create an array first.")
                else:
                    search_sort_filter(self.arr)

            elif choice == 5:

                if self.arr is None:
                    print("Please create an array first.")
                else:
                    statistics(self.arr)

            elif choice == 6:

                print("\nThank you for using NumPy Analyzer!")
                break

            else:
                print("Invalid choice. Please try again.")


# Create object
obj = DataAnalytics()

# Start program
obj.show_menu()