'''parking charge
Free for 2 hours, ₹20/hr (3–5 hrs), ₹50/hr (after 5 hrs).'''
hour=int(input("enter the hour "))
if hour==2:
    charge=0
elif hour>3 and hour<5:
    charge=20*hour
else:
    charge=50*hour
print("charge",charge)