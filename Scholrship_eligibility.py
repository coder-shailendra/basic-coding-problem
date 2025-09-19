"""scholarship eligibility
Eligible if marks ≥85 and income < ₹2,00,000."""
marks=int(input("enter the marks"))
income=int(input("enter the income" ))
if marks>=85:
    print("eligible")
elif income<200000:
    print("eligible")
else:
    print("not eligible")