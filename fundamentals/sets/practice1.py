# Write a program that continually asks the user 
# to enter characters until the user enters a 
# previously entered character or more than one 
# character at a time. After, the program should 
# print the number of unique characters that were 
# entered. Use a set to accomplish this

characters = set()

while True:
    character = input("Enter a character: ")
    if len(character) > 1:
        break

    if character in characters:
        break

    characters.add(character)

print(f"Number of unique characters entered: {len(characters)}")
