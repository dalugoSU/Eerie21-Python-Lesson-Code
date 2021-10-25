# Mad Libs!

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
