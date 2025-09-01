day=int(input("enter the day:"))
if day<=7:
    print("no fine")
elif day>8 and day<14:
    fine=day*5
    print("fine",fine)
elif day>15 and day<30:
    fine=day*10
    print("fine",fine)
else:
    print("membership cancelled")
