import random;

passed = 0
failed = 0
count = 0

for question in range(1, 11):
	first_operand = random.randint(1, 100)
	second_operand = random.randint(1, 100)

	question = input(f"{first_operand} + {second_operand} = ")
	answer = int(question)
	if answer == (first_operand + second_operand):
		passed = passed + 1
	elif answer != (first_operand + second_operand):
		failed = failed + 1
	count = count + 1	

print(f"You passed {passed} out of {count} questions")
print(f"You failed {failed} out of {count} questions")