"This is a string."
'This is also a string.'
'I told my friend, "Python is my favorite language."'
"The language 'Python' is named after Monty Python, not the snake."
"One of Pythin's strengths is its diverse and supportive community."

# changing the case
name = "ada lovelace"
print(name.title())
# UPPER CASE
print(name.upper())
# lower case
print(name.lower())

        # USING VARIABLES IN STRINGS

# F-strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
# OR
message = f"Hello, {full_name.title()}!"
print(message)

# Practice
first_name_1 = "muhammad"
middle_name_1 = "hamza"
last_name_1 = "ashraf"
city = "islamabad"
university = "national institute of psychology"
age = 24
height = 167

sentence = f"\nMy name is {first_name_1.title()} {middle_name_1.title()} {last_name_1.title()}. I am a resident of {city.title()} and I study at {university.title()}. My age is {age} and I have a height of {height} cm."
print(sentence + "\n") 
# SIMPLE ---^

# OR
sentence_1 = "My name is " + "{} {} {}".format(first_name_1, middle_name_1, last_name_1).title() + ". I am a resident of " + "{} ".format(city).title() + "and I study at" + " {}".format(university).title() + ". My age is" + " {} ".format(age) + "and I have a height of" + " {} ".format(height) + "cm.\n"
print(sentence_1) 
# COMPLEX ---^

# OR
sentence_2 = "My name is " + first_name_1.title() + " " + middle_name_1.title() + " " + last_name_1.title() + ". I am a resident of " + city.title() + " and I study at " + university.title() + ". My age is " + str(age) + " and I have a height of " + str(height) + " cm.\n"
print(sentence_2)
# MOST COMPLEX ---^


    # ADDING WHITESPACE TO STRINGS

# whitespace refers to any nonprinitng character
# \t --- for tab
# \n --- for new line

print("Python")
print("\tPython")
print("\t\tPython")
print("\t\t\tPython")
print("\t\t\t\tPython")
print("\t\t\tPython")
print("\t\tPython")
print("\tPython")
print("Python\n")

print("\nLanguages:\nPython\nC\nJavaScript\nRuby\nR")
print("\n\nLanguages:\n\tPython\n\tC\n\tJavaScript\n\tRuby\n\tR\n")


        # STRIPPING WHITESPACE

# rstrip() method --- to remove whitespace on right side of a string
# lstrip() --- to remove whitespace on left side of a string
# strip() --- to strip spaces from both sides

favorite_language = "python "
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language) # space not removed permanently

# to remove space permanently
favorite_language = "python "
favorite_language = favorite_language.rstrip() # associate the stripped value with the variable name
print(favorite_language)

favorite_language = " python "
print(favorite_language)
print(favorite_language.lstrip())
print(favorite_language.rstrip())
print(favorite_language.strip())