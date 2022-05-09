# Write a program that asks the user to enter a string 
# and prints the string's characters and their frequencies 
# in any order and in the following format: key: frequency

string = input("Enter a string: ")

character_frequencies = {}

for character in string:
    character_frequencies[character] = character_frequencies.get(character, 0) + 1

for key in character_frequencies:
    frequency = character_frequencies[key]

    print(f"{key}: {frequency}")
