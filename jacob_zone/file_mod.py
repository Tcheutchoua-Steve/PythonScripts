import tempfile
import sys


def extract_dictionary_data(filename) :
      dic_file = open(filename, 'r')
      for line in dic_file:
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
              #print(dict['host'])
              comp_dictionary.append(dict)



def modify_file(filename):

      #Create temporary file read/write
      t = tempfile.NamedTemporaryFile(mode="r+")

      #Open input file read-only
      i = open(filename, 'r')

      refkeyAdded = False ;
      #Copy input file to temporary file, modifying as we go
      for line in i:
          #print (line + 'good day Jesus')

          log_domain = line.split()[3]
          print(log_domain)
          for link in comp_dictionary :
              print(link['host'] + " and domain is " + log_domain)
              if link['host'] == log_domain :
                   t.write(line.rstrip()+ link['refkey'])
                   print ("\n \n"+ "written" + "\n ")
                   refkeyAdded = True
          if refkeyAdded == False :
              t.write(line.rstrip()+'\n')
              refkeyAdded = False ;


      i.close() #Close input file

      t.seek(0) #Rewind temporary file to beginning

      o = open(filename, "w")  #Reopen input file writable

      #Overwriting original file with temporary file contents
      for line in t:
           o.write(line)

      t.close() #Close temporary file, will cause it to be deleted

if __name__ == "__main__":
    comp_dictionary = []
    extract_dictionary_data("filename")
    modify_file(sys.argv[1])
    #modify_file("messages.txt")
      #print(comp_dictionary)


