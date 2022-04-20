#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
successful = 0
# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as kfile:

    # loop over the file
    for line in kfile:
    
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
        # the following elif agumentation MUST be AFTER we check for a fail
        # this statement assumes the if statement above it tested false
        elif "-] Authorization failed" in line: # can ONLY be true if the "if" was false!
            successful += 1

print("The number of failed log in attempts is", loginfail)

print("The number of sucessful log in attempts is", successful)
print(line.split(" ")[-1])
#keystone_file.close() # close the open file

