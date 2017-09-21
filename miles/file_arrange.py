#!/usr/bin/python3
#from itertools import zip
from itertools import islice

previous_line = None
with open('output4.txt') as lines:
    for line in lines:
        if line.startswith('great'):
            print (line + ''.join(islice(lines, 1)) + " wel done")
            p = [x[1] for x in line.split() if x.startswith('great')]
            print (p)
        previous_line = line

def extract_data(prev_line,line,next_line):
    output_line = None
    pass

# Pring text to specific columns python
#fhand.write('%s %+50s %+80s \n' % (id,name,email))
