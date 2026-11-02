class expensetracker:
    def __init__(self):
        self.expenses = []
        self.categories = []
        self.income = []

    def add_expense(self, amount, date, category):
    #need to add the expense to the expenses list based on the user's input for amount, date, and category

    def add_category(self, category):
    #need to add the category to the categories list based on the user's input for category


    def add_income(self, amount, date_range):
    #need to add the income to the income list based on the user's input for amount and date_range

    def list_expenses(self):
    #need to print the expenses list to the user

    def list_categories(self):
    #need to print the categories list to the user


def main():
    tracker = expensetracker()
    while True:
        print("Tyler's Expense Tracker Menu")
        print("1. Add Expense")
        print("2. Add Category")
        print("3. Add Income")
        print("4. List Expenses By Month")
        print("5. List Categories")
        print("6. Exit")

        selection = input("Please select an option (1-6): ")

        if selection == "6":
            print("Thank you! Closing the program now.")
            break


if __name__ == "__main__":
    main ()