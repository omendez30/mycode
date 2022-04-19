#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

# Your solution goes below this line
# ----------------------------------
munsters["episodes"] = 70

print(f"Characters are: {munsters.get('names')}")
print(f"Endate: {munsters.get('endDate')}")
print(f"Start date: {munsters.get('startDate')}")
print(munsters)

for x in munsters.get("names"):
    print(x, "is a character on the Munsters")
