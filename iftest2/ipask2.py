#!/usr/bin/env python3

ipchk = input("Apply an IP address: ")

if ipchk == "192.168.70.1":
    print(f"Looks like the IP address of the Gateway was set: {ipchk}")
elif ipchk: #if any data is provided, this will test true
    print(f"Looks like the IP address was set: {ipchk}")
else: #if data not provided
    print("You did nott provide input")
