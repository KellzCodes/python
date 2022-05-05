import random

def main():

	playerOne = input("Player One - Please enter your name: ")
	print(f"Hello, {playerOne} \n")

	playerTwo = input("Player Two - Please enter your name: ")
	print(f"Hello, {playerTwo} \n")

	p1 = 0
	winsPlayer1 = 0
	p2 = 0
	winsPlayer2 = 0
	rounds = 1

	while rounds != 4:
		print(f"Round {rounds}")
		p1 = roll_dice()
		p2 = roll_dice()
		print(f"{playerOne} Roll: {p1}")
		print(f"{playerTwo} Roll: {p2}")

		if p1 > p2:
			winsPlayer1 = winsPlayer1 + 1
			print(f"{playerOne} wins! \n")
		elif p2 > p1:
			winsPlayer2 = winsPlayer2 + 1
			print(f"{playerTwo} wins! \n")
		else:
			print("Draw! \n")

		rounds = rounds + 1

	if winsPlayer1 > winsPlayer2:
		print(f"{playerOne} Wins - Rounds Won: {winsPlayer1}")
	elif winsPlayer2 > winsPlayer1:
		print(f"{playerTwo} Wins! - Rounds Won: {winsPlayer2}")
	else:
		print("Draw!")

def roll_dice():
	dice = random.randint(1, 6)

	return dice

main()