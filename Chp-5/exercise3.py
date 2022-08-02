
usernames = [
    'hamzaaashraf', 'm_usama', 
    'hasan_433', 'haroon54',
    'saleh_a', 'shoaib.mohsin',
    'admin'
    ]

# 5-8 

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

print('\n')

# 5-9

if usernames:
    for username in usernames:
        print(f"Hello {username}!")
else:
    print("We need to find a user!")

print('\n')

usernames = [] # redifining the list

if usernames:
    for username in usernames:
        print("Hello {username}!")
else:
    print("We need to find a user!")

print('\n')


# 5-10

current_users = ['hamza12', 'Usman34', 'ZEESHAN21', 'JAWAD_H', 'Bashir_a']
new_users = ['ali_34', 'ahmed_khan', 'subhan21', 'hamza12', 'jawad_h']

for new_user in new_users:
    if new_user in current_users:
        print("""\nThe username you entered is not avaiable.
Kindly enter a new username.""")
    else: 
        print("\nThis username is avaiable.")

print('\n')


current_users_low = []

for current_user in current_users:
    current_users_low.append(current_user.lower())

new_users = ['ali_34', 'ahmed_khan', 'subhan21', 'HAMZA12', 'Jawad_h']

for new_user in new_users:
    if new_user.lower() in current_users_low:
        print("""\nThe username you entered is not available.
Kindly enter a new username""")
    else:
        print("\nThis username is avaiable.")

print('\n')


# 5-11

numbers = []
for value in range(1, 10):
    numbers.append(value)

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

print('\n')
