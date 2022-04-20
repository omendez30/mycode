#!/usr/bin/env python3

"""RZFeeser | Alta3 research nesting an if-statment inside of a for loop"""

# create a list of strings
vendors = ["cisco","juniper","big_ip","f5","arista","zach","stuart"]

# create a second list of strings
approved_vendors = ["cisco","juniper","big_ip"]

#loop across the list called vendors

for x in vendors:
    print(f"\nThe vendor is {x}", end=" ") # newline, print current vendor, and end without newline
    if x not in approved_vendors: # if x does not appear within the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end=" ")
print("\nOur loop has ended.")
