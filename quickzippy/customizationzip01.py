#!/usr/bin/env python3

import zipfile

def main():
    iszip = input("What is the file you want to examine (full or relative path)? ")

    if zipfile.is_zipfile(iszip): # returns true if the file is a zip file
        print("That's a zip file!")
    else:
        print("That's not a zip file")


main()
