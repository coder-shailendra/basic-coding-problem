"""bank account benefits
Input account type (Savings, Current, Salary) and print benefits."""
account_type = input("Enter account type (savings, current, salary): ")

if account_type == "savings":
    print("Benefits: Higher interest rate, ATM card, online banking")
elif account_type == "current":
    print("Benefits: Overdraft facility, unlimited transactions, business use")
elif account_type == "salary":
    print("Benefits: Zero balance, free debit card, salary credit")
else:
    print("Invalid account type entered!")