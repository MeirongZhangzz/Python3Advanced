account = 'qiyue'
password = '123456'

print('pls input account')
user_account = input()

print('pls input password')
user_password = input()

if account == user_account and password == user_password:
    print('success')
else:
    print('fail')
