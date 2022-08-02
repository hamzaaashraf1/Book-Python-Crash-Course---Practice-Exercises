for value in range(1, 21):
    print(value)

numbers = []
for value in range(1, 1_000_001):
    numbers.append(value)
    #print(value)
#print(numbers)

print(max(numbers))
print(min(numbers))
print(sum(numbers))

odd_numbers = []
for value in range(1, 20, 2):
    odd_numbers.append(value)
    print(value)

multiples_3 = [value for value in range(3, 31, 3)]
print(multiples_3)

# OR

multiples_3 = []
for value in range(3, 31, 3):
    multiple_3 = value
    multiples_3.append(multiple_3)
    print(multiple_3)

cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)
    print(cube)
print(cubes)

# OR

cubes = [value**3 for value in range(1, 11)]
print(cubes)

