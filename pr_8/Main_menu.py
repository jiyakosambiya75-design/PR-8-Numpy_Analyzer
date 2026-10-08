from Array_creation import array_creation
from Mathematical import mathematical_operations
from Combine_Split import combine_split
from Search_Sort import search_sort_filter
from statistics import statistics


class DataAnalytics:

    def __init__(self):
        self.arr = None

    def __check_array(self):

        if self.arr is None:
            print("Please create an array first.")
            return False

        return True

    @classmethod
    def create_analyzer(cls):

        return cls()

    @staticmethod
    def welcome_message():

        print("\n====================================")
        print("       Welcome to NumPy Analyzer")
        print("====================================")

    def show_menu(self):

        DataAnalytics.welcome_message()

        while True:

            print("\nChoose an option:")
            print("1. Create a NumPy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")

            try:

                choice = int(input("Enter your choice: "))

            except ValueError:

                print("Please enter a valid number.")
                continue

            if choice == 1:

                self.arr = array_creation()

                if self.arr is not None:
                    print("\nArray is stored successfully.")

            elif choice == 2:

                if self.__check_array():
                    mathematical_operations(self.arr)

            elif choice == 3:

                if self.__check_array():
                    combine_split(self.arr)

            elif choice == 4:

                if self.__check_array():
                    search_sort_filter(self.arr)

            elif choice == 5:

                if self.__check_array():
                    statistics(self.arr)

            elif choice == 6:

                print("\nThank you for using NumPy Analyzer!")
                break

            else:

                print("Invalid choice. Please try again.")


obj = DataAnalytics.create_analyzer()

obj.show_menu()