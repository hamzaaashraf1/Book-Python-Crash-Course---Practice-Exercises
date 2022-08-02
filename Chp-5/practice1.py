
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('\n')

# Conditional Tests --> an expression that can be tested for True or False
# if a conditional test is true, Python exexutes the code following the
# if statement. If the test is false, Pyhton ignores the code following
# the if statement

# Checking for Equality:

car = 'bmw' 
print(car == 'bmw') # whether the value of car is 'bmw'
# "==" ---> equality operator

car = 'Audi'
print(car == 'bmw')

# '=' --> se the value of car equal to 'audi'
# '==' --> is the value of car equal to 'bmw'

# Equality operator is Case Sensitive

car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')


# Checking for Inequality:
# Use the sign '!=' when testing for inequality

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!\n')


age = 20
print(age == 20)
print('\n')

age = 20
print(age != 20)
print('\n')

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!\n")

age = 19
print(age < 11)
print(age < 21)
print(age <= 21)
print(age > 15)
print(age>= 23)
print('\n')

# Checking Multiple Conditions

# Using 'and': (to check whether two conditions are simultaneously true)

age_0 = 22
age_1 = 18
print((age_0 >= 21) and (age_1 >= 21))
age_1 = 22
print((age_0 >= 21) and (age_1 >= 21))

# Using 'and': (to check whether either of the two conditions is true)

age_0 = 22
age_1 = 18
print((age_0 >= 21) or (age_1 >= 21))

age_0 = 18
print((age_0 >= 21) or (age_1 >= 21))
print('\n')

computers = ['hp', 'dell', 'sony', 'toshiba', 'acer', 'microsoft']
print('HP' in computers)
print('dell' in computers)
print('Acer' not in computers)
print('toshiba' not in computers)

my_fav = 'Dell'
print(my_fav in computers)
print(my_fav.lower() in computers)

my_fav2 = 'HP'
print(my_fav2.lower() in computers)
print(my_fav2 in computers)
print('\n')

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish."h)

print('\n')

