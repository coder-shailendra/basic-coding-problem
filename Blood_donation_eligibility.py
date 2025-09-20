'''blood donation eligibility
Eligible if age 18–60 and weight ≥50 kg.'''
age=int(input("enter the age:" ))
weight=int(input("enter the weight:"))
if age>18 and age<60 and weight>=50:
    print("eligible")
else:
    print("not eligible")