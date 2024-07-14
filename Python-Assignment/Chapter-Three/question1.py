passes = 0
failures = 0

for student in range(10):
	score = int(input("Enter a score (1 = pass and 2 = fail): "))

	if score == 1:
		passes = passes + 1
	elif score == 2:
		failures = failures + 1
	else:
		continue

print("The number of student that passed: ", passes)
print("The number of students that failed: ", failures)

if passes >= 8:
	print("Great Job!!! Bonus to the instructor")