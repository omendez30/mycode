#!/usr/bin/env python3

"""Alta3 Research | RZFeeser
   Conditionals - testing if strings test true"""

ipchk = input("Apply and IP address: ") #this line now prompts the user for input

# a provided string will test true

if ipchk:
    print(f"Looks like the IP address was set: {ipchk}")
else:
    print("You did not provide input.")
