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

#  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Intro to lists >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# A list is created like this
fruit_list = ["Apple", "Orange", "Berries"]

# We can use a for loop to print all items in a list
for fruit in fruit_list:
  print(fruit)


# We can index each element in a list with brackets and the index position

# Remember position 1 is at 0, and the last position is at -1

print(fruit_list[0]) # Apple
print(fruit_list[1]) # Orange
print(fruit_list[2]) # Berries

print(fruit_list[-1]) # Berries

# Be careful by indexing out of bounds, this will give an error because the item does not exist


# Let's practice

# Create a list of your choosing with as many elements as you'd like (String elements)

# Use a for loop to print all elements

# Use index to print first and last element


# Lists can also hold elemnts of different types


# List with different elements
random_list_elements = ["Hello", 5, False, ["No", 3.3]]

# Create an empty list
random_list = []

# How do we add elements to a list?
# We use the append function

# Adds at the end of your list

random_list.append(5) # Will add 5 at the end of the list
print(random_list) 

# Which removes at the end of your list

# We can delete the last item as well
random_list.pop() # will remove last item
print(random_list)

random_list.append(5) # 0
random_list.append(10) # 1
random_list.append(5) # 1

print(random_list)
# Which removes the first occurrence of the elemtn on the list
random_list.remove(5)
print(random_list)


# ACCESS WITH INDEX

print(f"First element: {random_list[0]}")

# Change element at position

random_list[0] = "CHANGED"

print(f"List after change: {random_list}")

# GRIDS

"""
Since lists can store other lists
we can create 'GRIDS' which can help
us visualize different tables
"""

tic_tac_toe_board = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

print(f"Tic tac toe: \n{tic_tac_toe_board}")

# How do we access??

"""
To access elements we think of rows and compile

Think of this grid

[][][]
[][][]
[][][]

as:

row 0   [col 0][col 1][col 2]
row 1   [col 0][col 1][col 2]
row 2   [col 0][col 1][col 2]

to access a 1D list we use index like this

test = [1, 2, 3]
test[0] <= access firsst element "1"

for a 2D list we use index like this [row][col]

test2 = [
  [1, 2, 3],
  [4, 5, 6]
]
test[0][1] <= access first row, second column "2"

"""

tic_tac_toe_board = [
  [0, 0, 0],
  [0, False, 0],
  [0, 0, 0]
]

# To access the item "False"

# Intro to functions

# define name_function()

# define
# parameters

# Add a second parameter
def greet(name, favorite_food):
  # Add print statement
  # Add it to print statement
  print(f"Hello {name} and your favorite is {favorite_food}")

# call your function
# put it here
greet(name="John Clancy", favorite_food="Cake")


# Add two parameters


"""
add_two_numbers(number_one=6, number_two=4):
  result = number_one (6) + number_two (4) # 10

  return result

"""

def add_two_numbers(num1, num2):
  result = num1 + num2
  return result



# Functions are blocks of reusable code

"""
FUNCTION TEMPLATE

def function_name(parameters(optional)):
  function body
  return statement (optional)
"""

"""
Let's say we want to create a function that adds
two numbers together.
"""


"""
To create a function we use the "def" keyword

then we name our function (in this case I named it add_two)

Then we place parenthesis, and if needed parameters.

Remember the fruit going into the blender? num1, and num2 in this case are the "fruit" in that scenario

Then we return a value (in this case the sum)
"""

# To use a function we "call it" by typing its name and giving it the "ingredients" it requires

"""

Things to review

* Functions can have multiple parameters or None
* Functions can have no return
* Once return is reached, function ends
* Functions can call other functions

"""

# Let's create a funciton that checks winner
def play_game(user, computer, user_wins, computer_wins):
  # Make our global variables accessible
  
  if user == "rock" and computer == "rock":
    print(f"It's Tie, {user_name}!")
  elif user == "rock" and computer == "paper":
    print(f"{user_name} lost!")
    computer_wins = computer_wins + 1
  elif user == "rock" and computer == "scissors":
    print(f"{user_name} wins!")
    user_wins = user_wins + 1
  elif user == "paper" and computer == "paper":
    print(f"It's Tie, {user_name}!")
  elif user == "paper" and computer == "rock":
    print(f"{user_name} wins!")
    user_wins = user_wins + 1
  elif user == "paper" and computer == "scissors":
    print(f"{user_name} lost!")
    computer_wins = computer_wins + 1
  elif user == "scissors" and computer == "scissors":
    print(f"It's Tie, {user_name}!")
  elif user == "scissors" and computer == "paper":
    print(f"{user_name} wins!")
    user_wins = user_wins + 1
  elif user == "scissors" and computer == "rock":
    print(f"{user_name} lost!")
    computer_wins = computer_wins + 1
  else:
    return
  
  return user_wins, computer_wins

# Sets

# Sets >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

a_set = {"Hello", False, "Hello"}
empty_set = set()

print(type(a_set))
print(f"A set: {a_set}")

# TURN list into a set >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

a_list = ["Hello", True, "Hello"]

another_set = set(a_list)
print(f"Another set: {another_set}")

# set operations
# print(dir(set))
# help(set.add)

# ADD an element >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

test_set = set() # empty set

print(f"Test set: {test_set}")

test_set.add(10)
test_set.add(True)
test_set.add("Hello World")
test_set.add(True)

# to add multiple elements at once
# accepts lists, strings, tuples as well as other sets as its arguments
test_set.update([False, "another", 21])

print(f"Test set after adding: {test_set}")

# REMOVE an element >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

test_set.remove(10)
print(f"Test set after removing 10: {test_set}")

# test_set.remove(20) << ERROR! KeyError, 20 is not in set

# GETTING an element >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# print(test_set[0]) ERROR! Not subscriptable

"""
Accessing a Set

You can loop through the set items using a for loop, or check if a  value is present in the set by using the in keyword.

"""
print("\n\nLooping Through test_set\n")
for item in test_set:
  print(item)

print(f"\nChecking if 20 in set: {20 in test_set}")

# Python Assesment 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import random

"""
Python Assesment!

For this python assesment you will be completing challenges.
These challenges will be modifying the code below.
Before starting the challenges make sure you look at the code and ask any questions if you have any!

Challenges:

1) Change the number of tries the user has until they lose
  - User tries is how many tries they have to get it right

2) Change the input message to get the user's asnwer
  - Example: "Please enter your guess: "

3) If the user got the wrong answer, tell them if they should guess higher or lower
  - HINT: Is the user guess greater or less than the actual number?

4) Right now, the random number is from 0 - 10. Change this range!
  - Example: 1 - 20

5) Print rules of the game before the game starts 
  - Rules: User has to guess number correctly
  - or ANYTHING YOU WANT

7) Write Comments on the "hashtags bellow" on what the code below or next to the hashtag is doing

8) Get the player's name before the game starts, save it in a variable and use it in the game messages.
  - Example: "You lost! McDonald"

9) Free Code! Add anything you'd like no restrictions

10) Add a comment below the game with the name of your favorite data structure. Also add one difference between a lists and a sets.

6) Create a function of your choosing at the end, bellow all the code. Call this function
  - Define a function: def functionName(AnyParametersHere):
  - Call function: functionName()
  

You Did it!

"""

# Your name: 


# CHALLENGE 5 Below this line


# CHALLENGE 7
number_of_tries_allowed = 5
player_name = input("Enter your name: ")

# CHALLENGE 7
while number_of_tries_allowed != 0:

  # CHALLENGE 7
  user_asnwer = input("Enter a number: ")
  random_number = random.randint(0, 10)

  # CHALLENGE 3 BELOW THIS LINE

  # CHALLENGE 7
  if int(user_asnwer) == random_number:
    print("Congrats! You got it")
    break # CHALLENGE 7
  else:
    print("That's wrong! try again...\n")
    number_of_tries_allowed -= 1 # CHALLENGE 7

  if number_of_tries_allowed == 0:
    print(f"You lost! The number was {random_number}")

# CHALLENGE 10 HERE


# Function here that prints hello, or something of your choosing Below this line

