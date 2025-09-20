'''ATM PIN Validation
Check if entered PIN is:
Exactly 4 digits-Check if correct PIN → Grant Access
Otherwise → Show Invalid PIN message'''
pin=int(input("enter the pin:"))

if pin==4:
    print("valid pin")
else:
    print("invalid pin")