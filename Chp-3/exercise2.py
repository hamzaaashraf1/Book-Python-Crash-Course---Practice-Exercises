guests = ['saad', 'ali', 'umar', 'haider']
print(guests)
print(f'''\nHey {guests[0].title()}, you are invited to dinner
    at my home on the coming Sunday.''')
print(f'''Hey {guests[1].title()}, you are ínvited to dinner
    at my home on the coming Sunday.''')
print(f'''Hey {guests[2].title()}, you are invited to dinner
    at my home on the coming Sunday.''')
print(f'''Hey {guests[3].title()}, you are invited to dinner
    at my home on the coming Sunday.\n''')
print(f"""Unfortunately, {guests[2].title()} couldn't
    make it to the party.\n""")

not_coming = 'umar'
guests.remove(not_coming)
guests.insert(2, 'zeeshan')

print(guests)
print(f'''\nHey {guests[0].title()}, you are invided to dinner
    at my home on the coming Sunday.''')
print(f'''Hey {guests[1].title()}, you are ínvited to dinner
    at my home on the coming Sunday.''')
print(f'''Hey {guests[2].title()}, you are invited to dinner
    at my home on the coming Sunday.''')
print(f'''Hey {guests[3].title()}, you are invited to dinner
    at my home on the coming Sunday.\n''')

print("""Fortunately, we just found a bigger table, so
    due to availability of more space, we'll be
    inviting three more guests.\n""")

print(guests)
guests.insert(0, 'hamza')
guests.insert(3, 'usama')
guests.append('hasan')
print(guests)
guests1 = guests.copy()
print(guests1)

print(f'''\nHey {guests[0].title()}, you are invited to 
    dinner at my home on the coming Sunday''')
print(f'''Hey {guests[1].title()}, you are invited to
    dinner at my home on the coming Sunday.''')
print(f'''Hey {guests[4].title()}, you are invited to
    dinner at my home on the coming Sunday.''')
print(f'''Hey {guests[2].title()}, you are invited to
    dinner at my home on the coming Sunday.''')
print(f'''Hey {guests[6].title()}, you are invited to
    dinner at my home on the coming Sunday.''')
print(f'''Hey {guests[3].title()}, you are invited to
    dinner at my home on the coming Sunday.''')
print(f'''Hey {guests[5].title()}, you are invited to
    dinner at my home on the coming Sunday.\n''')

print(guests1)
print(len(guests1))
print('''\nAhhh! unfortunately, due to some
    unprecedented circumstances, I'll be 
    able to invite only two people to dinner.\n''')

not_invited_1 = guests1.pop()
print(f'''\nHi {not_invited_1.title()}, I am so sorry
    I wouldn't be able to accomodate you in the party
    due to lack of space. Apologies!''')

not_invited_2 = guests1.pop()
print(f'''\nHi {not_invited_2.title()}, I am so sorry
    I wouldn't be able to accomodate you in the party
    due to lack of space. Apologies!''')
not_invited_3 = guests1.pop()
print(f'''\nHi {not_invited_3.title()}, I am so sorry
    I wouldn't be able to accomodate you in the party
    due to lack of space. Apologies!''')

not_invited_4 = guests1.pop()
print(f'''\nHi {not_invited_4.title()}, I am so sorry
    I wouldn't be able to accomodate you in the party
    due to lack of space. Apologies!''')

not_invited_5 = guests1.pop()
print(f'''\nHi {not_invited_5.title()}, I am so sorry
    I wouldn't be able to accomodate you in the party
    due to lack of space. Apologies!''')

print(f'''\nHey {guests1[1].title()}, you are still invited to
    the party. See you on Sunday.''')
print(f'''\nHey {guests1[0].title()}, you are still invited to
    the party. See you on Sunday!\n''')

print(guests1)
del guests1[1]
del guests1[0]
print(guests1)