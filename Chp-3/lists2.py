cars = ['suzuki cultus', 'honda civic', 'toyota corolla']
print(cars)
print('\n')

# Modifying Elements
cars[1] = 'nissan sunny' #element at index 1 replaced with new value
print(cars) 
cars[0] = 'toyota prius'
print(cars)
print('\n')

# Adding Elements
cars = ['suzuki cultus', 'honda civic', 'toyota corolla']
print(cars)
cars.append('nissan sunny')
print(cars)
cars.append('toyota prius')
print(cars)
print('\n')

# Adding Elements to Empty Lists
names = []
names.append('Hamza')
print(names)
names.append('Usama')
print(names)
names.append('Hammad')
print(names)
print('\n')

# Adding Element at Desired Position
cars = ['suzuki cultus', 'honda civic', 'toyota corolla']
print(cars)
cars.insert(0, 'toyota prius')
print(cars)
cars.insert(4, 'nissan sunny')
print(cars)
print('\n')

# Removing Elements (using 'del' statement)
cars = ['suzuki cultus', 'honda civic', 'toyota corolla']
print(cars)
del cars[2]
print(cars)
del cars[1]
print(cars)
del cars[-1]
print(cars)

cars = ['suzuki cultus', 'honda civic', 'toyota corolla']
print(cars)
del cars[0:2]
print(cars) #disadvantage: can't retrieve the deleted value
print('\n')

# Deleting an item in a way that its value can be used afterwards
cars = ['suzui cultus', 'honda civic', 'toyota corolla']
print(cars)
popped_car1 = cars.pop()
print(cars)
print(popped_car1)
popped_car2 = cars.pop()
print(cars)
print(popped_car2)
popped_car3 = cars.pop()
print(cars)
print(popped_car3)
print('\n')
cars = ['suzuki cultus', 'honda civic', 'toyota corolla']
last_car = cars.pop()
print(f"The last car I owned was a {last_car.title()}.")
print(cars)
print('\n')
cars = ['suzuki cultus', 'honda civic', 'toyota corolla']
first_car = cars.pop(0)
print(f"The first car I owned was a {first_car.title()}.")
print('\n')

# Removind an item by value/name
cars = ['suzuki cultus', 'honda civic', 'toyota corolla']
print(cars)
cars.remove('suzuki cultus')
print(cars)
#Also
cars = ['suzuki cultus', 'honda civic', 'toyota corolla']
print(cars)
too_expensive = 'honda civic' # we are assigning this value to a variable so
# that it may remain accessible even after it has been removed from the list.
cars.remove(too_expensive)
print(cars)
print(f"{too_expensive.title()} is too expensive for me to buy.")
print('\n')
