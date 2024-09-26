user_login = input('Login: ')
user_password = input('Password: ')

if user_login == 'x' and user_password == 'y':

    print('You are logged in')
    file = open('Computer Programming Exam Topics.txt', 'r')
    print(file.read())

else:

    while user_login != 'x' or user_password != 'y':
        print('Incorrect Login or Password', 'Try again')
        user_login = input('Login: ')
        user_password = input('Password: ')
    else:
        print('You are logged in')
        file = open('Computer Programming Exam Topics.txt', 'r')
        print(file.read())