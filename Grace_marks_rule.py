"""grace mark rule
If student fails by ≤5 marks, add grace marks, else fail."""
marks=float(input("enter the marks"))
if marks>50:
    print("pass")
elif marks>45 and marks<50:
    print("pass with grace marks")
else:
    print("fail")
    
