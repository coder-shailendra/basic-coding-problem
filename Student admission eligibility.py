maths=int(input("enter the maths marks:"))
physics=int(input("enter the physics marks:"))
chemistry=int(input("enter the chemistry:"))
total=maths+physics+chemistry
mp=maths+physics
if (maths>=65 and physics>=55 and chemistry>=50) and (total>=180 or mp>=140):
    print("student is eligible")
else:
    print("student is not eligible")