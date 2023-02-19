import os

# Define a dictionary to store budget data
budget = {}

# Define a function to add income or expenses to the budget
def add_transaction(amount, category, month, is_income):
    if month not in budget:
        budget[month] = {"income": {}, "expenses": {}}

    if is_income:
        if category in budget[month]["income"]:
            budget[month]["income"][category] += amount
        else:
            budget[month]["income"][category] = amount
    else:
        if category in budget[month]["expenses"]:
            budget[month]["expenses"][category] += amount
        else:
            budget[month]["expenses"][category] = amount

# Define a function to display the budget data for a specific month
def display_budget(month):
    if month in budget:
        print(f"Budget for {month}:")
        print("Income:")
        total_income = 0
        for category, amount in budget[month]["income"].items():
            print(f"{category}: ${amount:.2f}")
            total_income += amount
        print("Expenses:")
        total_expenses = 0
        for category, amount in budget[month]["expenses"].items():
            print(f"{category}: ${amount:.2f}")
            total_expenses += amount
        total_left = total_income - total_expenses
        print(f"Total left: ${total_left:.2f}")
    else:
        print(f"No budget data for {month}")

# Define a function to save the budget data to a file
def save_budget(filename):
    with open(filename, 'w') as f:
        for month, data in budget.items():
            f.write(f"{month}:\n")
            f.write("Income:\n")
            for category, amount in data["income"].items():
                f.write(f"{category},{amount}\n")
            f.write("Expenses:\n")
            for category, amount in data["expenses"].items():
                f.write(f"{category},{amount}\n")
    print(f"Budget data saved to {filename}")

# Define a function to load the budget data from a file
def load_budget(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            current_month = ""
            is_income = False
            for line in f:
                if line.endswith(":\n"):
                    current_month = line.strip()[:-1]
                elif line.startswith("Income:"):
                    is_income = True
                elif line.startswith("Expenses:"):
                    is_income = False
                else:
                    category, amount_str = line.strip().split(',')
                    amount = float(amount_str)
                    add_transaction(amount, category, current_month, is_income)
        print(f"Budget data loaded from {filename}")
    else:
        print(f"{filename} does not exist, starting with empty budget")

# Load the budget data from a file
filename = "budget_data.txt"
load_budget(filename)

# Define a loop to allow the user to add transactions and display the budget
while True:
    print("1. Add income")
    print("2. Add expense")
    print("3. Display budget")
    print("4. Save budget")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        category = input("Enter income category: ")
        month = input("Enter month (e.g. Jan 2023): ")
        add_transaction(amount, category, month, True)

    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        month = input("Enter month (e.g. Jan 2023): ")
        add_transaction(amount, category, month, False)
    elif choice == "3":
        month = input("Enter month to display (e.g. Jan 2023): ")
        display_budget(month)
    elif choice == "4":
        save_budget(filename)
    elif choice == "5":
        save_budget(filename)
        print("Exiting program...")
        break
    else:
        print("Invalid choice, please try again")
