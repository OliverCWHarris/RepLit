#declaring username and password variables
user_name=str(input('enter a username: '))
password=str(input('enter a password: '))

#asks if you want to keep what you entred, displayes what you entred
save=str(input('save credentials? (y/n)' + 'username: ' + user_name + ' password: ' + password + ': '))

#decision making for what happens if you save credentials
if save == 'y':
    print('verify credentials:')
    user_name_check=str(input('enter username: '))
    password_check=str(input('enter password: '))

    if user_name_check == user_name and password_check == password:
        print('correct credentials, saved loggin')
    else:
        print('invalid credentials, aborting...')
        quit()
elif save == 'n':
    print('credentials not saved, exiting...')
    quit()
else:
    print('syntax error, exiting...')