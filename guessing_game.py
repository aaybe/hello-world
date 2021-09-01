import random

random_number = random.randint(1,10)
num_tries = 3

print("This is a guessing game. I have chosen a number betwen 1 and 10.")

while num_tries > 0:
	print(f"Number of tries left = {num_tries}")
	guess = input("Enter you guess: ")
	guess = int(guess)
	if (guess > 10) or (guess < 0):
		print("Invalid number! Number must be between 0 and 10")
	elif guess == random_number:
		break
	elif guess < random_number:
		print("Your number is too low")
	else:
		print("Your number is too high")
	num_tries -= 1

if num_tries == 0:
	print("You lost the game :(")
else:
	print("Congrats you won the game!")