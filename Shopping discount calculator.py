bill=int(input("enter total bill amount:"))

if bill>=5000:
    discount=0.2*bill
    
elif bill>=2000 and bill<5000:
    discount=0.1*bill

else:
    discount=0*bill

final_amount=bill-discount

print("final payable amount:", final_amount)