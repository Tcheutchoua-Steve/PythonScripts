import sys
iteration = 0
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


def handleSolver():
    global size
    global mailboxes

    initializeVars()

    mailboxes = ['c']*size
    print(str(mailboxes) )


    for i in range(0,size):
        if (i%2 ==0 ):
            mailboxes[i] = 'c'
        else :
            mailboxes[i] = 'O'
    print(str(mailboxes))
    iteration = 2

    mailboxes_string = ' '.join(str(mailboxes_item) for mailboxes_item in mailboxes )
    mailboxes_string_lower = mailboxes_string.lower()
    mailboxes = mailboxes_string_lower.split()
    while iteration < size:
        for i in range(iteration,size,iteration):
            if ((mailboxes[i] is 'c') or  (mailboxes[i] is'C')) :
                mailboxes[i] = 'O'
            elif (mailboxes[i] is 'o' or (mailboxes[i] is 'O')) :
                mailboxes[i] = 'C'
            #print("new mb" + str(mailboxes))
        print(str(mailboxes) + " iteration is " + str(iteration))
        #mailboxes = [item.lower() for item in mailboxes]
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
            size = int(input ("Please enter the size of mailboxes :"))
            break
        except :
            print ('Please Enter a valid option')


    # <editor-fold desc="Description">
'''    with open('output'+str(sze)+'.txt',"w+") as output:
        output.write(str(mailboxes))
        print(str(mailboxes))
    for i in range(0,sze,2):
        if i % 2 == 0 :
            mailboxes[i] = 'O'
    with open('output'+str(sze)+'.txt',"a") as output:
        output.write('\n'+str(mailboxes))
        print(str(mailboxes))
    # </editor-fold>
'''

if __name__ == "__main__": main_menu()
