# Intro to python ----------------------------------------------------------------------------

# <- This is a single line comment

"""
This is a
multiline comment
"""

# Let's learn Data Types

# [ Integers ] => Numbers!
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# [ Floats ] => Numbers with decimals!
# 1.1, 2.2, 32.5, 6.42, 23.53

# [ Booleans ] => is it true, false?
# True, False

# [ strings ] => a combination of characters!
# "hello", "this is a sentence"

# [ Character ] => a single character
# 'a', 'v', 'c'

# Our first python Code

print("Hello, World")
# What data type is "Hello, World?"

# You can also print the contents of a variable
# We will look into this more deeply soon

# Variables

# String


my_school = "Syracuse University"
print(my_school)

# Variables can also hold numbers
my_age = 22 # Python naming convention
two = 2

# You can set a variable equal to another variable
 
new_number = my_age

print(new_number)

# You can do math with saved numbers
another_number = my_age // two # 22 * 2 = 44
print(another_number)

# To print you use the print keyword
print() # <= you put parenthesis

# Different print methods

# You can also print strings along with variables
print("My name is:", my_age)
print("My name is: " + my_name)

# F(ormat) strings

age = 22

print(f"My name is: {my_name} and my age is {age}") 
# <= can also be written like this

# Saving boolean into a variable

is_cold = True
is_weekend = False

print(is_weekend)

# You can compare integers, and strings
# You can use operators such as: >, <, ==, is not

# 5 > 4 = True
# 5 == 5 = True
# 10 < 6 = False

print(f"Is tesla equal to tesla: {'tesla' == 'tesla'}")
print(f"Is 5 greater then 2: {5 > 2}")
print(f"Is 10 less than 6: {10 < 6}")



# Mad Libs! ----------------------------------------------------------------------------------

# First we gather all information from our user

gender = input("Tell me, a boy or girl, and click enter: ")
name = input("Give me a name for your character, and click enter: ")
building = input("Tell me what kind of building did the person live in?, and click enter: ")
enemy = input("Tell me a kind of enemy, it can be a monster, animal etc. and click enter: ")
weapon = input("Pick your choice of weapon, and click enter: ")

# Then we print a space
print("\n\n")


# Now we print the story with the words we saved

print("Once upon a time, there was a", gender, "whose name was", name, ".")
print(name, "lived in a", building, ".")
print("One day, all of a sudden,", name, "'s ", building, "was under attack.")
print(name, "goes and grabs his", weapon, "and attacks the", enemy, ". ")
print("Upon defeating the", enemy, ",", name, "is hailed as a hero by everyone.")

# Different ways to print!
name = "Fluffy"

print("Hello" + name)
print("Hello", name)
print(f"Hello {name}")

