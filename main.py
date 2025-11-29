import os

if not os.path.exists("demofile.txt"):
    with open("demofile.txt", "w") as f:
        f.write("0\n")

with open("demofile.txt") as f:
    balance = int(f.readline())
    remaining_lines = f.readlines()


def add_income():
    global balance
    income = int(input("Income Amount: "))
    balance = balance + income
    return income


def add_expense():
    global balance
    expense = int(input("Cost: "))
    balance = balance - expense
    return expense


my_income = add_income()
my_expense = add_expense()

print(f"Income: {my_income}")
print(f"Expense: {my_expense}")

with open("demofile.txt", "a") as f:
    f.write(f"Income is {my_income}, Expenses are {my_expense}\n")

with open("demofile.txt", "w") as f:
    f.write(str(balance) + "\n")
    for line in remaining_lines:
        f.write(line)

with open("demofile.txt") as f:
    print(f.read())
