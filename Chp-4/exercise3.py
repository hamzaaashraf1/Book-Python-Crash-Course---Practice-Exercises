
cities = ['Islamabad', 'Lahore', 'Karachi', 'Peshawer', 'Quetta']

print("The first three items in the list are:")
print(cities[:3])

print("\nThree items from the middle of the list are:")
print(cities[1:4])

print("\nThe last three items in the list are:")
print(cities[2:])
print('\n')

pak_cities = cities[:]

cities.append('Faisalabad')
pak_cities.append('Gujranwala')

print(f"The cities of Pakistan are:")
for city in cities:
    print(city)
print("\nAlso, the cities of Pakistan are:")
for city1 in pak_cities:
    print(city1)
print('\n')


for city in cities:
    print('Here is a city of Pakistan:')
    print(city)
print('\n')
for city1 in pak_cities:
    print("Here is a city of Pakistan:")
    print(city1)