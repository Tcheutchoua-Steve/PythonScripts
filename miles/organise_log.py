#!/usr/bin/python3
#This script goes through a set of logs and produces a resulting file containing some extracted data from the file.
from itertools import islice
import re
import sys
import argparse

generated_line = None
#dl = dh = cpl = cph = gl = gh  = None
def filterfile (log_file, output_file) :
    global generated_line

    searchString = "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    previos_line = None
    with open(log_file) as log:
        with open(output_file,"w+") as output:
            output.write("%-35s   %-35s  %-35s  %-35s  %-20s\n" % ("Field","County","Depth","Cumm PROD","Gravity"))
            output.write('*'*165 +'\n')
            for line in log :
                if line.strip().startswith(searchString):
                    line_before_slice = line
                    nextLine = ''.join(islice(log, 1))
                    if(extractData(previos_line,line_before_slice,nextLine)):
                        output.write(generated_line)
                        print(generated_line)
                previos_line = line



def extractData(previous, current, next):
    global generated_line

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

    generated_line = "%-35s   %-35s  %-35s  %-35s  %-20s\n" % (str(field).strip(), str(county).strip(), str(depth).strip(), str(cumm_prod).strip(), str(gravity).strip())

    if((int(depth) >= dl) and (int(depth)<dh) and (int(cumm_prod) >= cpl) and (int(cumm_prod) < cph) and (int(gravity) >= gl) and (int(gravity) < gh)):
        return True

    return False


if __name__ == "__main__":
    global dl ; global dh ; global cpl ; global cpl ; global gl ; global gh
    ##********************************* Parsing User input with options and arguments *********************************######
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='An application to extract data from files.')

    # Required positional argument
    parser.add_argument('-i', type=str, required=True, help='path and name of the input file to run')
    parser.add_argument('-o', type=str, required=True, help='path and name of the output file to use')
    parser.add_argument('-dl', type=int, default=0, help='path and name of the log file to use')
    parser.add_argument('-dh', type=int, default=sys.maxsize, help='path and name of the log file to use')
    parser.add_argument('-cpl', type=int, default=0, help='path and name of the log file to use')
    parser.add_argument('-cph', type=int,default=sys.maxsize, help='path and name of the log file to use')
    parser.add_argument('-gl', type=int, default=0, help='path and name of the error file to use')
    parser.add_argument('-gh', type=int, default=sys.maxsize,help='path and name of the error file to use')

    args = parser.parse_args()
    if args.i is None :
        print ('Please provide the path and name of the input file with logs , -- help for more info')
        sys.exit()

    if args.o is None :
        print ('Please provide the path and name of the output file to use , -- help for more info')
        sys.exit()

    """
    if args.f is None :
        print ('Please provide the path and name of the syslog file to use , -- help for more info')
        sys.exit()

    if args.e is None :
        print ('Please provide the path and name of the error file to use , -- help for more info')
        sys.exit()
    """

    inputlog_file = args.i
    output_file = args.o
    dl = args.dl
    dh = args.dh
    cpl = args.cpl
    cph = args.cph
    gl = args.gl
    gh = args.gh

    filterfile(inputlog_file,output_file)
