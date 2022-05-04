import random

def computerGuess(lowval, highval, randnum, count = 0):
	if highval >= lowval:
		guess = lowval + (highval - lowval) // 2
		# If guess is in the middle, it is found!
		if guess == randnum:
			return count
		# if "guess" is greater than the number,
		# it must be found in the lower half of the set of numbers
		# between the lower value and the guess
		elif guess > randnum:
			count = count + 1
			return computerGuess(lowval, guess - 1, randnum, count)
		else:
			count = count + 1
			return computerGuess(guess + 1, highval, randnum, count)

	else:
		# number not found
		return -1


# generate a random number between 1 and 100
randnum = random.randint(1, 101)

count = 0
guess = -99

while(guess != randnum):
	# Get the user's guess
	guess = (int) (input("Enter your guess between 1 and 100: "))

	if guess < randnum:
		print("higher")
	elif guess > randnum:
		print("lower")
	else:
		print("you guessed it!")
		break
	count = count + 1
# end of while loop
print(f"You took {count} steps to guess the number")
print(f"computer took {computerGuess(0, 100, randnum)} steps!")