#!/usr/bin/env python3

#documentation is found at http://api.open-notify.org/astros.json

import requests

DATA = "http://api.open-notify.org/astros.json"

def main():
    #Send HTTPS GET to the API
    getresp = requests.get(DATA)

    #Decode response
    get_data = getresp.json()

    #print response
    #print(get_data)
    ppl_inspace = str(get_data["number"])
    print(f"People in space {ppl_inspace}")
    
    #loop across response
    for astronauts in get_data['people']:
        name = astronauts['name']
        craft = astronauts['craft']
        
        print(f"{name} is on the {craft}")


if __name__ == "__main__":
    main()
