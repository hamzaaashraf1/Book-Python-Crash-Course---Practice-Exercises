# Tuples --> immutable; values can't be changed

# dimensions of a rectangle
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print(dimensions[:])
print(dimensions[0:])
print(dimensions[:2])
print(dimensions[-1])
print(dimensions[-2])
print(dimensions[-2:])
print(dimensions[:-1])

# dimensions[0] = 200 # ---> results in error b/c elements of a tuple can't be changed
# print(dimensions)

#  in a tuple with a single element, the element should be followed
# by a comma

my_t = (5,)
print(my_t)
my_t2 = (2)
print(my_t2)
print('\n')

# looping through a tuple using a for loop

dimensions2 = (56, 67)
for dimension in dimensions2:
    print(dimension)
print('\n')

# writing over a tuple
# a tuple can't be modified but a new value can be assigned to
# a variable that represents a tuple

dimensions3 = (234, 744)
print('Original dimensions:')
for dimension in dimensions3:
    print(dimension)  

dimensions3 = (534, 123) # python doesn't raise any errors , because
# reassigning a variable is valid.
print('\nModified dimensions:')
for dimension in dimensions3:
    print(dimension)
print('\n')

