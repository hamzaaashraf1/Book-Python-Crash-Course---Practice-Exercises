
ages = [24, 18, 23, 17, 15]

for age in ages:
    if age >= 18:
        print(f"\nAs your age is {age}, you are eligible to cast your vote.")
        print("Have you registered to vote yet?")
    else:
        print(f'''\nAs you are uner eighteen({age}), you are not eligible to cast
your vote. Please register to vote as soon as you turn 18!''')
print('\n')


ages = [4, 18, 24, 66]

for age in ages:
    if age <= 4 or age > 65:
        print("Your admission is free so you don't need to pay any charges.")
    elif age <= 18:
        print("Your admission cost is Rs. 100")
    elif 18 < age <= 65:
        print("Your admission cost is Rs. 150.")
    # else:
    #     print("Your admission is free so you don't need to pay any charges.")
print("\n")

for age in ages:
    if age <=4 or age > 65:
        price = 0
    elif age <= 18:
        price = 100
    elif 18 < age <= 65:
        price = 150
    print(f"Your admission cost is Rs. {price}\n")


requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
print('\n')

# Another way
for requested_topping in requested_toppings:
    if requested_topping == "mushrooms":
        print("Adding mushrooms.")
    if requested_topping == "pepperoni":
        print("Adding pepperoni")
    if requested_topping == "extra cheese":
        print("Adding extra cheese.")
print("\nFinished making your pizza!")