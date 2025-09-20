charges=int(input("enter the charge:"))
day=int(input("enter the day:"))
if charges==2000/day:
    print("deluxe:")
elif charges==3000/day:
    print("super deluxe:")
elif charges==5000/day:    
    print("suite:")
elif day>5:
    print("10% discount")
else:
    print("any class")