from random import randint

def ask_question():
	while True:
		num1 = randint(1, 9)
		num2 = randint(1, 9)
		correct_answer = num1 * num2
		while True:
			answer = int(input(f"What is {num1} times {num2}?: "))
			if answer == correct_answer:
				print("Very good!")
				break
			else:
				print("No. Please try again.")

		play_again = input("Do you want to try another question? (yes/no): ").strip().lower()
		if play_again != 'yes':
			print("Thank you for practicing! Goodbye.")
			break

ask_question()
