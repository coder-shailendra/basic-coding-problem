unit=int(input("enter the unit"))
if unit<=100:
    charge=5*unit
elif unit>100 and unit<=200:
    charge=7*unit
elif unit>300:
    charge=10*unit
else:
    fixed_charge=unit*10+100
    charge=fixed_charge
    print(charge)