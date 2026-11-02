class expensetracker:
    def __init__(self):
        self.expenses = []
        self.categories = []
        self.income = []

    def add_expense(self, amount, date, category):
        if category not in self.categories:
            print("Category does not exist. Adding category to the list.")
            self.categories.append(category)
        self.expenses.append({"amount": amount, "date": date, "category": category})
        print("Expense added successfully. Returning to menu.")

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)
            print(f"Category '{category}' added successfully.")
        else:
            print(f"Category '{category}' already exists.")


    def add_income(self, amount, date_range):
        pass
        #need to add the income to the income list based on the user's input for amount and date_range

    def list_expenses(self):
        pass
        #need to print the expenses list to the user

    def list_categories(self):
        print(f"Existing categories: {self.categories}")
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

        if selection == "1" or selection.lower() == "add expense":
            amount = float(input("Enter the amount of the expense: "))
            date = input("Enter the date of the expense (MM-DD-YYYY): ")
            category = input("Enter the category of the expense: ")
            tracker.add_expense(amount, date, category)

        if selection == "2" or selection.lower() == "add category":
            while True:
                category = input("Enter the name of the new category: ")
                if category in tracker.categories:
                    print(f"Category '{category}' already exists. Please enter a different category.")
                else:
                    tracker.add_category(category)
                    keep_adding = input("Add another category?: ")
                    if keep_adding.lower() != "yes":
                        break
            tracker.add_category(category)

        if selection == "5" or selection.lower() == "list categories":
            tracker.list_categories()

        if selection == "6" or selection.lower() == "exit":
            print("Thank you! Closing the program now.")
            break


if __name__ == "__main__":
    main ()