#!/usr/bin/python3
# Exepctations can be gotten from https://www.upwork.com/jobs/~01c25b5935cf7e66bb

# Declaring variables that will be used widely
size = None
mailboxes = []
def main_menu() :

    #Request valid integer input until obtained
    while True:
        try:
            option = int(input ("Welcome to the POSTMAN console.\nPlease Enter 1 to solve the problem and 2 to exit"))
            break
        except :
            print ('Please Enter a valid option')

    # Deciding what to do based on input option selected
    if option == 1 :
        handleSolver()
        main_menu()
    elif option == 2 :
        Sys.exit
    else :
        print('This is not a valid option')
        main_menu()

#Solving the postman problem
def handleSolver() :
    global size
    size = initializeVars()
    with open('output'+str(size)+'.txt',"a") as output:
        n= 0
        for i in range(1,size) :
            for j in range(i*n,size/n,i) :
                if j < size-1 and mailboxes[j].lower == 'c':
                    mailboxes[j+1] = 'O'
                elif j < size-1 and mailboxes[j].lower == 'o':
                    mailboxes[j+1] = 'C'
                else:
                    raise ('There is a problem with the content of the mailbox')
                output.write('\n'+str(mailboxes))
                print(str(mailboxes))
                n += 1
        #output.write('\n'+str(mailboxes))

def initializeVars() :
    global mailboxes
    sze = 0
    while True:
        try:
            sze = int(input ("Please enter the size of mailboxes"))

        except :
            print ('Please Enter a valid option')
    mailboxes = ['c']*sze

    with open('output'+str(sze)+'.txt',"w+") as output:
        output.write(str(mailboxes))
    print(str(mailboxes))
    for i in range(0,sze,2):
        if i % 2 == 0 :
            mailboxes[i] = 'O'
    with open('output'+str(sze)+'.txt',"a") as output:
        output.write('\n'+str(mailboxes))
    print(str(mailboxes))

    return sze

if __name__ == "__main__": main_menu()
#def toggleCharacter(valid_chars , character) :
 #   if len(valid_chars == 2 and character in valid_chars):

