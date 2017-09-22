import tempfile
import sys
import argparse


def extract_dictionary_data(filename) :
    dic_file = open(filename, 'r')
    for line in dic_file:
        #create a dictionary of inputs for each line of the dictionary
        dict = {}
        line = line.split(',')

        if line[0][-3:] == 'com':
            #print line
            dict['FQDN']=line[0].strip()
            dict['domain'] = line[1].strip()
            dict['refkey'] = line[2].rstrip()
            dict['ipAdd'] = line[3].rstrip()
            #comparing the FQDN and domain name to get the hostName
            dict['host'] = line[0][:-len(line[1])][:-1]

            comp_dictionary.append(dict)


def modify_file(syslog_f,output_f,error_f):

    #Create temporary file read/write
    t = tempfile.NamedTemporaryFile(mode="r+")


    i = open(syslog_f, 'r')  #Open syslog file as input file
    o = open(output_f, "w")  #Open output file as to store data and modificationd done
    e = open(error_f,"w")    #Open error file to record domains not found

    #Manipulate every line of the syslog file and analyse to determine action
    for line in i:

        refkeyAdded = False ;  # Temporary variable to help determine if a refkey has been added to the file
        log_domain = line.split()[3]   # Getting the domain from the syslog file
        for link in comp_dictionary :
            if link['FQDN'] == log_domain :    # Comparing the domain in syslog and domains in the dictionary file
                if "refnum" in line.split()[-1] :#Checking if refnum already exist in the line indicated and updating the refnum
                    line = line.rpartition(' ')[0] #Removing the previous refNum so that the line is updated below
                o.write(line.rstrip()+ " refnum:"+link['refkey']+"\n") #Printing the output file with new refKey
                refkeyAdded = True    # Set indicator variable to true,indicating that a match has been found
        # If refKeyAdded is false, then the syslog domain have not been found in the dictionary file
        if refkeyAdded == False :
            o.write(line.rstrip()+'\n')
            e.write(line.rstrip()+ "\n")



    i.close() #Close input file

    t.seek(0) #Rewind temporary file to beginning
    t.close() #Close temporary file, will cause it to be deleted
    e.close()

if __name__ == "__main__":

    ##********************************* Parsing User input with options and arguments *********************************######
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Optional app description')
    # Required positional argument
    parser.add_argument('-d', type=str, help='path and name of the dictionary to use')
    parser.add_argument('-f', type=str, help='path and name of the log file to use')
    parser.add_argument('-o', type=str, help='path and name of the output file to use')
    parser.add_argument('-e', type=str, help='path and name of the error file to use')

    args = parser.parse_args()
    if args.d is None :
        print ('Please provide the path and name of the dictionary to use , -- help for more info')
        sys.exit()
    dictionary_file = args.d
    if args.f is None :
        print ('Please provide the path and name of the syslog file to use , -- help for more info')
        sys.exit()
    syslog_file = args.f
    if args.o is None :
        print ('Please provide the path and name of the output file to use , -- help for more info')
        sys.exit()
    output_file = args.o
    if args.e is None :
        print ('Please provide the path and name of the error file to use , -- help for more info')
        sys.exit()
    error_file = args.e
    print("dictionary is " + dictionary_file + " syslog is " + syslog_file)

    comp_dictionary = []
    extract_dictionary_data(dictionary_file)
    modify_file(syslog_file,output_file,error_file)



