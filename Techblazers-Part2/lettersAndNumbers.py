users_input = input("Enter a sentence: ")

count_integers = 0
count_letters = 0

for character in users_input:
	if character.isdigit():
		count_integers += 1
	elif character.isalpha():
		count_letters += 1
print("Letters:", count_letters)
print("Numbers:", count_integers)