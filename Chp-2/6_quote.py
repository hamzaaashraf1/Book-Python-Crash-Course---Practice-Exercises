# July 21, 2022
# MUhammad Hamza Ashraf
# A quote by my favorite scientist!

print('''Albert Einstein once said, "A person who never made a mistake
    never tried anything new."\n''')

famous_person = "Albert Einstein"

message = f'''{famous_person} once said, "A person who never made
a mistake never tried anything new."\n'''

message_2 = "{}".format(famous_person) + ''' once said, "A person who never made 
a mistake never tried anything new."\n'''

message_3 = famous_person + ''' once said, "A person who never made a mistake
never tried anything new."\n'''

print(message)
print(message_2)
print(message_3)

name = "\nHamza\t"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())