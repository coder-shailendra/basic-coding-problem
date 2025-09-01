password=(input("enter the passwor:"))
length=len(password)
if length<6:
    print("password is weak")
elif length>6 and length<10:
    print("password is medium strength")
else:
    print("password is strong")
