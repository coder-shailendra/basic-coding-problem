import math
print("===== CALCULATOR =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus / Remainder")
print("6. Power")
print("7. Square Root")
print("8. Cube")
print("9. Percentage")
print("10. Floor Division")
choice = int(input("Enter your choice: "))
if choice == 7:
    num = float(input("Enter number: "))
    print("Square Root =", math.sqrt(num))
elif choice == 8:
    num = float(input("Enter number: "))
    print("Cube =", num ** 3)
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == 1:
        print("Result =", num1 + num2)
    elif choice == 2:
        print("Result =", num1 - num2)
    elif choice == 3:
        print("Result =", num1 * num2)
    elif choice == 4:
        print("Result =", num1 / num2)
    elif choice == 5:
        print("Remainder =", num1 % num2)
    elif choice == 6:
        print("Power =", num1 ** num2)
    elif choice == 9:
        print("Percentage =", (num1 / 100) * num2)
    elif choice == 10:
        print("Floor Division =", num1 // num2)
    else:
        print("Invalid choice")