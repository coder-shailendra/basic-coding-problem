'''Simple Calculator
Perform +, -, ×, ÷ depending on operator entered'''
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
operator=input("enter operator (+, -, *, /): ")
if operator=="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
    result=num1*num2
elif operator=="/":
    if num2!=0:
        result=num1/num2
    else:
        result="Error! Division by zero."
else:
    result="Invalid operator!"
print("result",result)