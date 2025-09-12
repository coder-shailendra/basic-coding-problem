marks=int(input("enter the marks:"))
if marks>=95:
    print("distinction")
elif marks>=90:
    print("grade A+")
elif marks>=75 and marks<=89:
    print("grade A")
elif marks>60 and marks<74:
    print("grade B")
elif marks>50 and marks<59:
    print("grade C")
elif marks>35 and marks<49:
    print("grade D")
else:
    print("fail")