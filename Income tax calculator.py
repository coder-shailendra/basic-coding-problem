amount=int(input("enter the amount"))
if amount< 250000:
    tax=0
elif amount>250001 and amount<500000:
    tax=.05*250000
elif  amount>500001 and amount<1000000:
    tax=(.2*500000)+12500
else:
    tax=(.3*1000000)+112500
print("tax",tax)