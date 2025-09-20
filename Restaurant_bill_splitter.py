total_bill = float(input("Enter total bill amount: ₹"))
friends = int(input("Enter number of friends: "))

if friends >= 4:
    total_bill = total_bill * 0.90   # 10% discount

share = total_bill / friends

print("\nFinal Bill: ₹", round(total_bill, 2))
print("Each person should pay: ₹", round(share, 2))