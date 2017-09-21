#!/usr/bin/python3

import sys

# Declaring variables that will be used widely
iteration = 0
#size of the mailbox
size = None
#The stores that are to be openned or closed.
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


def handleSolver():
    global size
    global mailboxes

    initializeVars()

    mailboxes = ['c']*size
    print(str(mailboxes) )

    iteration = 2

    while iteration < size+1:
        for i in range(iteration,size+1,iteration):
            if ((mailboxes[i-1] is 'c') or  (mailboxes[i-1] is'C')) :
                mailboxes[i-1] = 'O'
            elif (mailboxes[i-1] is 'o' or (mailboxes[i-1] is 'O')) :
                mailboxes[i-1] = 'C'
            #print("new mb" + str(mailboxes))
        print(str(mailboxes))
        #mailboxes = [item.lower() for item in mailboxes]

        #convert the mailbox to lower case letters
        mailboxes_string = ' '.join(str(mailboxes_item) for mailboxes_item in mailboxes )
        mailboxes_string_lower = mailboxes_string.lower()
        mailboxes = mailboxes_string_lower.split()
        #print('new mailbox is' + str(mailboxes))
        iteration = iteration + 1

def initializeVars() :
    global mailboxes
    global size
    while True:
        try:
            size = int(input ("Enter number of rows: "))
            break
        except :
            print ('Please Enter a valid option')

if __name__ == "__main__": main_menu()
