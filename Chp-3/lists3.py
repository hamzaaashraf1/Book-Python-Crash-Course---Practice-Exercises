names = ['hamza', 'saad', 'ali', 'usama', 'zeeshan', 'haider', 'hasan']
print(names)

# Sorting a list permanently
names.sort() # default is alphabetical order
print(names)
names.sort(reverse=True) # reverse alphabetical order
print(names)
print('\n')

# Sorting a list temporarily
names_2 = ['hamza', 'saad', 'ali', 'usama', 'zeeshan', 'haider', 'hasan']
print('Here is the original list:')
print(names_2)
print('\nHere is the sorted list:')
print(sorted(names_2))
print('\nHere is the list sorted in reverse alphabetical order:')
print(sorted(names_2, reverse=True))
print('\nHere is the original list again:')
print(names_2)
print('\n')

# Reverse the order of a list
names_3 = ['hamza', 'saad', 'ali', 'usama', 'zeeshan', 'haider', 'hasan']
print(names_3)
names_3.reverse()
print('\n')
print("this is the names' list in reverse order:")
print(names_3)
print('\n')
print("reversing again:")
names_3.reverse()
print(names_3)
print('\n')

# finding the length of a list

print(len(names))
print(len(names_2))
print(len(names_3s))
