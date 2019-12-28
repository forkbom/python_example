import getpass
username = input('Username:')
password = getpass.getpass('password:')

if username == 'bob' and password == '123456':
    print('congratulation')
else:
    print('Sorry Bye bye')