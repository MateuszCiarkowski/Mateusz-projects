import subprocess

user_login = None
user_password = None

while user_login != 'x' or user_password != 'y':
    print('Incorrect Login or Password\nTry again')
    user_login = input('Login: ')
    user_password = input('Password: ')
else:
    print('You are logged in')
    subprocess.call(['C:\\Windows\\system32\\notepad.exe', 'Computer Programming Exam Topics.txt'])




