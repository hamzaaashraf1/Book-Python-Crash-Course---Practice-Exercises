players = ['Afridi', 'Babar', 'Rizwan', 'Yasir', 'Hasan', 'Shadab']
print(players[0:3])
print(players[:3])
print(players[3:6])
print(players[3:])
print(players[:])
print(players[:4])
print(players[0: :3])

print('\n')

print('Here are the first three players of the Pakistani team:')
for player in players[:3]:
    print(player)

print(players)
print('\n')
players1 = players[:]
print(players)
print(players1)
print('\n')
players.append('Ahmed')
players1.append('Faizan')
print(players)
print(players1)
print('\n')

players2 = players
print(players)
print(players2)
print('\n')
players2.append('Mohsin')
print(players2)
print(players)
