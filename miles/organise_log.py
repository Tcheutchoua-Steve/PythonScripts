#!/usr/bin/python3
#This script goes through a set of logs and produces a resulting file containing some extracted data from the file.
from itertools import islice
import re

def filterfile (log_file, output_file) :

    searchString = "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    previos_line = None
    with open(log_file) as log:
        with open(output_file,"a+") as output:
            for line in log :
                if line.strip().startswith(searchString):
                    line_before_slice = line
                    nextLine = ''.join(islice(log, 1))
                    formed_line = extractData(previos_line,line_before_slice,nextLine)
                    #output.write(formed_line)
                    #print(formed_line)
                previos_line = line



def extractData(previous, current, next):
    #Extract cummulative production in the current line
    cumm_prod = current.split()[-1]
    #print(str(current.split()[-1]))
    # Extract gravity from next line
    #gravity = [x.replace(",GRAV:",'') for x in next.split() if x.startswith(',GRAV')]
    gravity = re.search(',GRAV:\s*[0-9]+', next).group(0).replace(',GRAV:','')

    # Extract field, depth and county in the previous line
    #depth = [previous.split()[i]  for i,j in enumerate(previous.split()) if re.match('^,DEPTH:\s*[0-9]+', j.upper())]
    depth = re.search(',DEPTH:\s*[0-9]+', previous).group(0).replace(',DEPTH:','')
    #county = [' '+previous.split()[i-2] + ' '+ previous.split()[i-1] for i,j in enumerate(previous.split()) if j.startswith(',DEPTH:')]
    temp_line = previous[0:previous.find(',DEPTH:')].split()[::-1]
    county_temp = [temp_line[:i+1]   for i,x in enumerate(temp_line) if re.match(r'\d+',x)]
    #print(str(temp_line))
    county = ' '.join(county_temp[0][::-1])
    print(county)
    #field = previous.split(county[0].strip())[0]
    #print(str(field) + " and county:" + str(county[0].strip())+ "\n")


    #return "%s %+50s %+50s  %+50s %+50s\n" % (str(field).strip(), str(county).strip(), str(depth).strip(), str(cumm_prod).strip(), str(gravity).strip())
    #print(" Field: %-35s   County: %-35s  Depth: %-35s  Cumm PROD: %-35s  Gravity: %-20s\n" % (str(field).strip(), str(county).strip(), str(depth).strip(), str(cumm_prod).strip(), str(gravity).strip()))
    return "good"


if __name__ == "__main__": filterfile("oilsch_1.txt","output.txt")
