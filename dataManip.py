

#
comp_dictionary = []

#Creating our comparison dictionary
dic_file = open("dict-referencenumber.txt", 'r')
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

## The comp_dictionary is now updated with all of the domains, hosts and others.
print (comp_dictionary)

for i in comp_dictionary :
    print(i['FQDN'])


print (comp_dictionary)
