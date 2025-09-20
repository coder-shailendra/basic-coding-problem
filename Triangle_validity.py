'''Triangle Validity
Input 3 sides and check if valid triangle.'''
a= float(input("enter the side a:"))
b= float(input("enter the side b:"))
c= float(input("enter the side c:"))
if (a+b)>c and (b+c)>a and (a+c)>b:
    print("valid triangle")
else:
    print("not valid triangle")
    