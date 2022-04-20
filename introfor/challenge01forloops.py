#!/usr/bin/env python3


def main():
    
    """On this farm there was a..."""

    # this is the data we want to loop across
    # it is a list containing 3 dictionaries

    farms = [{"name": "NE Farm", "agriculture":["sheep","cows","pigs","chickens","llamas","cat"]},{"name": "W Farm", "agriculture":["pigs","chickens","llamas"]},{"name": "SE Farm", "agriculture":["chickens", "carrots","celerey"]}]
    # each time through the loop
    # farm will be equal to one of the dict within the list "farms"

    for farm in farms:
        print(farm.get("name", "Unknown Farm"), end=":\n") # this is like saying, "farm['name']"
         # only it will not return an error

        for agri in farm.get("agriculture"): # from a single "farm" get the list from the key "agriculture"
            print(" -", agri) # each time through the list "agriculture", print out an item


main()

