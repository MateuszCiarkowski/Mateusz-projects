import subprocess

user_login = None
user_password = None

while __name__ == "__main__":
    user_login = input('Login: ')
    user_password = input('Password: ')
    if user_login == 'x' and user_password == 'y':
        print('You are logged in')
        subprocess.call(['notepad', 'Computer Programming Exam Topics.txt'])
        break
    else:
        print('Incorrect Login or Password\nTry again')




