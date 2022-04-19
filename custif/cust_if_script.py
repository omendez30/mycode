#!/usr/bin/env python3

score = float(input("Pleas enter a score: "))

if score <= 100 and score >=90:
    print("You received an A")
elif score < 90 and score >= 80:
    print("You received a B")
elif score < 80 and score >= 70:
    print("You received a C")
elif score < 70 and score >= 60:
    print("You received a D")
else:
    print("Try harder, F")
