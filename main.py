def add_income():
    income = input("Income Amount: ")
    return income


def add_expense():
    expense = input("Cost: ")
    return expense


my_income = add_income()
my_expense = add_expense()

print(f"Income: {my_income}")
print(f"Expense: {my_expense}")
