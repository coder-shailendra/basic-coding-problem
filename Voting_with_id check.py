"""Voting with ID Check
Allow voting if age ≥18 and has valid ID"""
age=float(input("enter the age"))
if age>=18:
    print("eligible for voting")
else:
    print("minor or not eligible for voting")