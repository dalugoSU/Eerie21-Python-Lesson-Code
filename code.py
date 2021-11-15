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


# Conditionals >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Let's learn conditionals

# Let's walk through a program that tells you if you need an umbrella or not

is_raining = True

# Now let's write our conditional
if is_raining == True:
  print("Bring an umbrella!")
else:
  print("It's sunny outside!")

print("")

# You can chain as many conditions as you'd like
# using the keyword elif

name = "daniel"
user_guess = input("Guess my name: ")

if user_guess == name:
  print("You got it right!")
elif user_guess == "mike":
  print("interesting guess but not it!")
else:
  print("Wrong! Try again")

print("")

# As you can see I added another condition
# by using "elif"
# Notice how else does not use a condition
# It just executes if nothing else works

# You can check multiple conditions in one line

# Slides =>>>>

# AND: both have to be true
# OR: only one needs to be true
# NOT: The opposite (if true then false)

# Let's write a program that checks whether it
# is the weekend and it's not raining

is_raining = False
is_weekend = True

if is_raining == False and is_weekend == True:
  print("Let's go outside!")

# You can also just use the name of the variable
# to check for boolean
if is_raining or is_weekend: 
  print("One of those is true!")

# Now I will check for is_raining
if not is_raining:
  print("It's not raining!")

print("")


# Intro to Loops >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# There are two types of loops that we will focus on
# While loops
# For loops

# A for loop looks like this
print("\nA for loop: ")
for number in range(1, 11):
  print(number)

# You can print things in a sequence like a string
name = "Daniel"
print("\nMy name letter by letter: ")
for letter in name:
  print(letter)


# for something in something do something

# A while loop looks like this
print("\nA while loop: ")
count = 1
while count <= 5:
  print(count)
  count = count + 1

# Notice how we have a condition. Out loop will run
# until the condition is met!
# NOTE: Careful with while loops, if the condition
# is never met, then we could end up with an infinate
# loop ( A loop that never ends )

# For this reason:

# For loops are good when we know how many times we want the loop to repeat

# While loops are good when we do not know how many times we want the loop to repeat

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Guess the number! >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import random

user_name = input("What is your name: ")
print("")

guesses_taken = 0
number_to_guess = random.randint(1, 20)

print(f"{user_name}, I am thinking of a number between 1 and 20! You have 5 tries to get it right :D ")
print("")

while True:

  user_guess = int(input("Enter your guess: "))
  guesses_taken = guesses_taken + 1

  if user_guess < number_to_guess:
    print("Your guess is too low.\n")
  elif user_guess > number_to_guess:
      print("Your guess is too high.\n")
  elif user_guess == number_to_guess:
      print(f"You got it {user_name}! You figured it out in {guesses_taken} tries!\n")
      break
  
  if guesses_taken == 5:
    print("You are out of tries!\n")
    break

print("")
