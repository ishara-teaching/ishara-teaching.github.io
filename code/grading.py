#! /usr/bin/env python

import sys
import csv

# Read in the CSV file.
cdata = csv.reader(file(sys.argv[1]))
data = []
for x in cdata: data.append(x)

names = data[0][1:]
fields = data[1:]

# Process all of the student names.
i = 0
print "\n"
for n in names:
    i += 1
    t = 0
    
    # Print the student's name first.
    print n
    
    # Now go through the criteria.
    for x in fields:
        f = x[0]
        g = x[i]
        
        # If "f" is a criterion, print it.
        if f.startswith("*"):
            print "\n"+f
        
        # If "g" is a feedback, print it.
        elif g != "":
            if (g in f) and f != "": print " ] ",f
            else: print " ] ",g
            
            try: t += int(g.split()[-1])
            except: pass
    
    print "\nTOTAL = ",t
    
    # Block for input (you can comment this line out to get a single file of output).
    f = raw_input()
    print "\n"

