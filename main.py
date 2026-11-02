class expensetracker:
    def __init__(self):
        self.expenses = []
        self.categories = []

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

    def list_expenses(self):
        def expense_sort_key(expense):
            return expense["date"]
        sorted_expenses = sorted(self.expenses, key=expense_sort_key)
        print("Expenses sorted by date:")
        for expense in sorted_expenses:
            print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}")
        total_expense = sum(expense["amount"] for expense in sorted_expenses)
        print(f"Total expenses: {total_expense}")

    def list_categories(self):
        print(f"Existing categories: {self.categories}")


def main():
    tracker = expensetracker()
    while True:
        print("Tyler's Expense Tracker Menu")
        print("1. Add Expense")
        print("2. Add Category")
        print("3. List Expenses By Month")
        print("4. List Categories")
        print("5. Exit")

        selection = input("Please select an option (1-5): ")

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

        if selection == "3" or selection.lower() == "list expenses by month":
            tracker.list_expenses()

        if selection == "4" or selection.lower() == "list categories":
            tracker.list_categories()

        if selection == "5" or selection.lower() == "exit":
            print("Thank you! Closing the program now.")
            break


if __name__ == "__main__":
    main ()