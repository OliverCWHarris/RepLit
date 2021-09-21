#declaring and entering username and password variables
user_name=str(input('enter a username: '))
password=str(input('enter a password: '))



#asks if you want to keep what you entred, displayes what you entred
save=str(input('save credentials? (y/n): '))



#decision making for what happens if you save credentials
if save == 'y':
    #ask you to reenter your credentials
    print('verify credentials:')

    user_name_check=str(input('enter username: '))

    password_check=str(input('enter password: '))


    #if the username and password you entred matches what you entred earier it is saved
    #else it errors out and exits
    if user_name_check == user_name and password_check == password:
        print('correct credentials, saved loggin')

        write_username=user_name+'\n'
        write_password=password+'\n'
        usernames = open("usernames.txt","w")
        usernames.writelines(write_username)
        usernames.close()

        passwords = open("passwords.txt","w")
        passwords.writelines(write_password)
        passwords.close()

    else:
        print('invalid credentials, aborting...')
        quit()



#however if you dont save it, the program will just exit without saving
elif save == 'n':
    print('credentials not saved, exiting...')
    quit()
else:
    print('syntax error, exiting...')