#!/usr/bin/python3
#This script goes through a set of logs and produces a resulting file containing some extracted data from the file.
from itertools import islice
import re

def filterfile (log_file, output_file) :

    searchString = "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    previos_line = None
    with open(log_file) as log:
        with open(output_file,"a+") as output:
            output.write("%-35s   %-35s  %-35s  %-35s  %-20s\n" % ("Field","County","Depth","Cumm PROD","Gravity"))
            output.write('*'*165 +'\n')
            for line in log :
                if line.strip().startswith(searchString):
                    line_before_slice = line
                    nextLine = ''.join(islice(log, 1))
                    formed_line = extractData(previos_line,line_before_slice,nextLine)
                    output.write(formed_line)
                    print(formed_line)
                previos_line = line



def extractData(previous, current, next):
    #Extract cummulative production in the current line
    cumm_prod = current.split()[-1]

    # Extract gravity from next line
    gravity = re.search(',GRAV:\s*[0-9]+', next).group(0).replace(',GRAV:','')

    # Extract field, depth and county in the previous line
    # Some Depths don't have a space between the depth string column and the figure
    depth = re.search(',DEPTH:\s*[0-9]+', previous).group(0).replace(',DEPTH:','')
    temp_line = previous[0:previous.find(',DEPTH:')].split()[::-1]
    county_temp = [temp_line[:i+1]   for i,x in enumerate(temp_line) if re.match(r'\d+',x)]
    county = ' '.join(county_temp[0][::-1])
    field = previous.split(county[0].strip())[0]



    return "%-35s   %-35s  %-35s  %-35s  %-20s\n" % (str(field).strip(), str(county).strip(), str(depth).strip(), str(cumm_prod).strip(), str(gravity).strip())
    return "good"


if __name__ == "__main__": filterfile("oilsch_1.txt","output.txt")
