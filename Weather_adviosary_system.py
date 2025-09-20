'''Weather Advisory System
If temperature <10 and raining → “Carry umbrella & warm clothes”. Else → Normal message.'''
temperature=float(input("enter the temperature"))
weather=input("enter the weather")
if temperature<10 and weather=="raining":
    print("carring umbrella and warm clothes")
else:
    print("normal message")