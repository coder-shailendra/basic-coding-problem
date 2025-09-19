'''Loan Eligibility Checker
Eligible if salary ≥ 25,000 and CIBIL ≥ 700.''' 
salary=int(input("enter the salary"))
if salary>=25000 and salary>=700:
    print("eligible") 
else:
  print("not eligible")