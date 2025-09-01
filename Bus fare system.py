year=int(input("enter the year:"))
ticket_price=float(input("enter the ticket price:"))
if year<5:
    fare=0*ticket_price
elif year>5 and year<17:
    fare=0.5*ticket_price
elif year>18 and year<60:
    fare=1*ticket_price
else:year>60
fare=0.75*ticket_price
print("total payable fare:",fare)