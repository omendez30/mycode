#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():
    #collect string input form the user
    user_input = input("Please enter an IPv4 IP address:")

    ## the line below created a single string taht is passed to print()
    #print("you told me the IPv4 address is: " + user_input)

    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)

    vendor = input("Please input the vendor name: ")
    print(vendor)

main()
