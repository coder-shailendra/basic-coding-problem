temp=int(input("enter the temp"))
if temp<0:
    print("freezing")
elif temp>0 and temp<20:
    print("cold")
elif temp>21 and temp<35:
    print("normal")
elif temp>35 and temp<45:
    print("hot")
else:
    print("heatwave alert")