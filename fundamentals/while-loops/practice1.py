# Write a program that continually asks the user to enter a number 
# Until the enter the number 5, at which point the program should
# print how many numbers the user has entered

number_of_entries = 0

while True:
    number = int(input("Enter a number: "))
    number_of_entries += 1

    if number == 5:
        break

print(f"You entered {number_of_entries} numbers.") 
