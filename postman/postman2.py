#!/usr/bin/python3
# Exepctations can be gotten from https://www.upwork.com/jobs/~01c25b5935cf7e66bb

import sys

# Declaring variables that will be used widely
size = None
mailboxes = []
def main_menu() :

    #Request valid integer input until obtained
    while True:
        try:
            option = int(input ("Welcome to the POSTMAN console.\nPlease Enter 1 to solve the problem and 2 to exit\n"))
            break
        except :
            print ('Please Enter a valid option')

    # Deciding what to do based on input option selected
    if option == 1 :
        handleSolver()
        main_menu()
    elif option == 2 :
        sys.exit
    else :
        print('This is not a valid option')
        main_menu()

#Solving the postman problem
def handleSolver() :
    global size
    global mailboxes
    size = initializeVars()
    mailboxes = [item.lower() for item in mailboxes]
    #print("initial mailbox is " + str(mailboxes))

    with open('output'+str(size)+'.txt',"a") as output:
        #n= 0
        j=1
        i = 2
        for i in range(2,size,1) :
            print('i is %d and j is %d '% (i,j))
            for j in range(i, size,1) :
                print('i %d size %d int(size/i) %d, j %d'%(i,size, int(size/i),j))
                if (j%i == 0) :
                    if j < size and mailboxes[j+1].lower() == 'c':
                        mailboxes[j+1] = 'O'
                    elif j < size and mailboxes[j+1].lower() == 'o':
                        mailboxes[j+1] = 'C'
                    else:
                        print(str(mailboxes[j]))
                        raise Exception('There is a problem with the content of the mailbox')
                #j+=i
                output.write('\n'+str(mailboxes))
                print(str(mailboxes))

                mailboxes = [item.lower() for item in mailboxes]
            print("loop is " +str(i))

def initializeVars() :
    global mailboxes
    sze = 0
    while True:
        try:
            sze = int(input ("Please enter the size of mailboxes: "))
            break
        except :
            print ('Please Enter a valid option')
    mailboxes = ['c']*sze

    with open('output'+str(sze)+'.txt',"w+") as output:
        output.write(str(mailboxes))
    print(str(mailboxes))
    for i in range(0,sze-1,2):
        if i % 2 == 0 :
            mailboxes[i+1] = 'O'
    with open('output'+str(sze)+'.txt',"a") as output:
        output.write('\n'+str(mailboxes))
    print(str(mailboxes))

    return sze

if __name__ == "__main__": main_menu()
#def toggleCharacter(valid_chars , character) :
 #   if len(valid_chars == 2 and character in valid_chars):

