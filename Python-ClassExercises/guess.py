from random import randint

player = randint(1, 1000)

counter = 0

guess = 0

while guess != player:
	guess = int(input("Guess my number between 1 and 1000: "))
	if guess < 1 and guess > 1000:
		print("Pls, enter a valid number between 1 and 1000")
	elif guess >= 1 and guess <= 1000:
		if guess == player:
			print("Congratulations, you guessed the number!!!")
		elif guess > player:
			print("Too high. Try again!!!")
		elif guess < player:
			print("Too low. Try again!!!")

	counter = counter + 1

if counter < 10:
	print(f" Well done Champ!!!, You made {counter} attempts")
else:
	print(f"You made {counter} attempts. You can do better next time")

