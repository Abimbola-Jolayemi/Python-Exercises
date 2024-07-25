passes = 0
failures = 0

for index in range(0, 15):
	score = int(input("Enter a score: "))

	if score >= 45:
		passes = passes + 1
	else:
		failures = failures + 1

print(passes, "students passed the examination")
print(failures, "students failed the examination")