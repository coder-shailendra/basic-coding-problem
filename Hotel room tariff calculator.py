charges=int(input("enter the prices:"))
day=int(input("enter the days:"))
if charges==2000/day:
    print("deluxe:")
elif charges==3000/day:
    print("super deluxe:")
elif charges==5000/day:    
    print("suite:")
else:
    print("5days,give .1* discount")