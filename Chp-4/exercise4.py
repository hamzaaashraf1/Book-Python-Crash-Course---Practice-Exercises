
foods = ('biryani', 'nihari', 'pulao', 'kheer', 'salad')

print('Our buffet restaurant offers following foods:')
for food_item in foods:
    print(food_item.title())

# foods[3] = 'custard'
# print('Here is the modified menu:')
# for item in foods:
#     print(item.title()) ----------> gives error

foods = ('biryani', 'karahi', 'zarda', 'roast', 'fish')
print('\nHere is the modified menu:')
for item in foods:
    print(item.title())


