'''courier charges
Charges: ≤1kg = ₹50, 1–5kg = ₹100, 5–10kg = ₹200, >10kg = Not Allowed'''
weight=int(input("enter the weight" ))
if weight<=1:
   pcharge=50
elif weight>1 and weight<5:
    charge=100
elif weight>5 and weight<10:
    charge=200
else:
 charge="not allowed"
 print("charge")
         
