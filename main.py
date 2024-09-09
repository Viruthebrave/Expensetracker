# Personal Expense Tracker

# Initialize an empty dictionary to store expenses
expenses = {}

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g. Food, Transport, etc.): ")
    amount = float(input("Enter the amount: "))

    if date in expenses:
        expenses[date].append({"category": category, "amount": amount})
    else:
        expenses[date] = [{"category": category, "amount": amount}]

def view_expenses():
    for date, expense_list in expenses.items():
        print(f"Expenses for {date}:")
        for expense in expense_list:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}")

def total_expenses():
    total = sum(sum(expense['amount'] for expense in expense_list) for expense_list in expenses.values())
    print(f"Total expenses: {total}")

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()