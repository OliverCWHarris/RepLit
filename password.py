import time


#creating account function
def create():

    global user_name
    global password
    #declaring and entering username and password variables
    user_name=str(input('enter a username: '))
    password=str(input('enter a password: '))



    #asks if you want to keep what you entred, asks you to resubmit for verification
    global save
    save=str(input('save credentials? (y/n): '))

    if save == 'y':
        #ask you to reenter your credentials
        print('verify credentials')

        user_name_check=str(input('enter username: '))

        password_check=str(input('enter password: '))


        #if the username and password you entred matches what you entred earier it is saved
        #else it errors out and exits
        if user_name_check == user_name and password_check == password:
            print('correct credentials, saved loggin')

            write_username=user_name+'\n'
            write_password=password+'\n'
            usernames = open("usernames.txt","a")
            usernames.writelines("\n")
            usernames.writelines(write_username)
            usernames.close()

            passwords = open("passwords.txt","a")
            passwords.writelines("\n")
            passwords.writelines(write_password)
            passwords.close()

            menu()



        else:
            print('invalid credentials, aborting...')
            run=0
            quit()
    
    #however if you dont save it, the program will just exit without saving
    elif save == 'n':
        print('credentials not saved, exiting...')
        run=0
        quit()
    else:
        print('syntax error, exiting...')


    

#login function
def login():
    print("enter credentials:")
    global login_check_u
    login_check_u=str(input("enter username: "))
    global login_check_p
    login_check_p=str(input("enter pasword: "))

    #opening files for login checks

    un=open("usernames.txt","r")
    readfile=un.read()
    pw=open("passwords.txt","r")
    readfile2=pw.read()
    if login_check_u in readfile and login_check_p in readfile2:
        print("success! logged in.")
        un.close()
        pw.close()
    else:
        print("invalid credentials, exiting...")
    
    #end of login checking




#delete account function
def delete():
    print("sorry this isnt implemeted yet!")


#menu printing function
def menu():

    print('Welcome to [brand name] account setup!')
    time.sleep(1)
    print('Please select what you would like to do')
    time.sleep(1)
    print('1 - create new account')
    time.sleep(1)
    print('2 - log into existing account')
    time.sleep(1)
    print('3 - delete account')
    menu_pt2()


#dump function to show all usernames and passwords
def dump():
    with open('usernames.txt') as e:
        print(e)
    with open('passwords.txt') as f:
        print(f)

#decision making function for the menu
def menu_pt2():
    global menu_choice
    menu_choice=input(': ')

    if menu_choice == '1':
        create()
    elif menu_choice == '2':
        login()
    elif menu_choice == '3':
        delete()
    elif menu_choice == 'd':
        dump()





menu()