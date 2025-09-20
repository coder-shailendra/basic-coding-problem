'''Cricket Match Result
Input runs of two teams and declare winner or tie.'''
team1=input("enter the team 1 runs")
team2=input("enter the team2 runs")
if team1>team2:
    print("team1 winner")
elif team1==team2:
    print("match tai")
else:
    print("team 2 winner")