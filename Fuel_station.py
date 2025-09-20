fuel=int(input("enter the fuel"))
money=int(input("entyer the money"))
if fuel>=20:
    discount=(money*.05)
    final_bill=money-discount
    print("5% discount on the money")
else:
    discount=0
    final_bill=money
    print("no discount")
    print("Final_bill")
