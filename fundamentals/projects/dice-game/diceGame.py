import random

def main():

	playerOne = input("Player One - Please enter your name: ")
	print(f"Hello, {playerOne} \n")

	playerTwo = input("Player Two - Please enter your name: ")
	print(f"Hello, {playerTwo} \n")

def roll_dice():
	dice = random.randint(1, 6)

	return dice

main()