for numbers in range(1, 6):
    print(numbers)
print('\n')
for values in range(7):
    print(values)
print('\n')

numbers = list(range(1, 6))
print(numbers)
print('\n')

# Using range() function to make a list of numbers
even_numbers = list(range(0, 101, 2))
print(even_numbers)
print('\n')

odd_numbers = list(range(1, 100, 2))
print(odd_numbers)
print('\n')

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
print('\n')

squares_1 = []
for value in range(1, 11):
    squares_1.append(value ** 2)
    #print(squares_1)

print(squares_1)
print(max(squares_1))
print('\n')

squares_2 = [value**2 for value in range(1, 11)]
print(squares_2)
print('\n')

numbers = list(range(1, 6))
print(numbers)

# print(help(range))

cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)

print(cubes)

cubes = []
for value in range(1, 11):
    cubes.append(value**3)

print(cubes)

cubes = [value**3 for value in range(1, 11, 1)]
print(cubes)