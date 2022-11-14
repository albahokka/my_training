# Присваиваем список переменной и производим
users = ['admin', 'egor', 'morfeus', 'clouse', 'HOWARD']

for user in users:
    if user == 'admin':
        print(f'Hello, {user.lower()}, would u like  to see a status report?')
    else:
        print(f'Hello, {user.lower().title()}, thank you for logging '
              f'in again.')

if len(users) == 0:
    print('We need to ind some users')
else:
    del users[0:]
    print(users)
    print('We need to ind some users')