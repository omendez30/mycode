#!/usr/bin/env python3
import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) #prints the ip address
            print("IP: ",end="")

            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]["addr"])
        except:
            print("Could not collect adapter information")


