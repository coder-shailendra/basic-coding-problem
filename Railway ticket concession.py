age=int(input("enter the age"))
if age<5:
    fare=0
elif age>=60:
    fare=.5
elif age>=18 and age<=59:
    fare=.02
else:
    fare=1   
print("final fare",fare)