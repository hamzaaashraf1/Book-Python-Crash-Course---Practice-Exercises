
# 5-3

print('\n')
alien_color = 'red'
if alien_color == 'green':
    print("The player just earned 5 points.")
alien_color = 'green'
if alien_color == 'green':
    print("The player just earned 5 points.")

# 5-4

print('\n')
alien_color = 'red'
if alien_color == 'green':
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points.")

alien_color = 'yellow'
if alien_color == 'yellow':
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points.")

# 5-5

print('\n')
alien_color = 'green'
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points")
else: 
    print("THe player earned 15 points.")

alien_color = 'red'
if alien_color == 'green':
    print('The player just earned 5 points.')
elif alien_color == 'yellow':
    print("The player just earned 10 points.")
else: 
    print("The player just earned 15 points.")

alien_color = 'yellow'
if alien_color == 'green':
    print("The player just earned 5 points.")
elif alien_color == 'yellow':
    print("The player just earned 10 points.")
else:
    print("The player just earned 15 points.")

# 5-6

print('\n')
age = 24
if age < 2:
    print("The person is a baby.")
elif 2 <= age < 4:
    print("The person is a toddler.")
elif 4 <= age < 13:
    print("The person is a kid.")
elif 13 <= age < 20:
    print("The person is a teenager.")
elif 20 <= age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

# 5-7

print('\n')
favorite_fruits = ['banana', 'orange', 'mango']
if 'strawberry' in favorite_fruits:
    print("You really like strawberries!")
if 'orange' in favorite_fruits:
    print('You really like oranges!')
if 'grapes' in favorite_fruits:
    print("You really like grapes!")
if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'mango' in favorite_fruits:
    print('You really like mangoes!')