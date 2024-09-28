from pathlib import Path

user_login = None
user_password = None

while user_login != 'x' or user_password != 'y':
    print('Incorrect Login or Password\nTry again')
    user_login = input('Login: ')
    user_password = input('Password: ')
else:
    print('You are logged in')
    p = Path(__file__).with_name('Computer Programming Exam Topics.txt')
    with p.open('r') as f:
        print(f.read())



