salary=float(input("enter the salary:"))
survice=int(input("enter the survice:"))
if survice>10:
        bonus=0.1*salary
elif survice>6 and survice<10:
        bonus=.08*salary 
else:
    bonus=.05*salary
    print("your bonus is:",bonus)
