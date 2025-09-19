'''internet speed test
Speed categories: <2 = Slow, 2–10 = Average, 10–50 = Fast, >50 = Superfast.'''
speed=int(input("enter the speed" ))
if speed<2:
    print("slow")
elif speed>2 and speed<10:
    print("average")
elif speed>10 and speed<50:
    print("fast")
else:
    print("superfast")