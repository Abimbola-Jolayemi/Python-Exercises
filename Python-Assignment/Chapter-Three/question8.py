max_number = 0
min_number = float('inf')
count = 0
total = 0

for index in range(0, 4):
	number = int(input("Enter a number: "))
	if number < min_number:
		min_number = number
	if number > max_number:
		max_number = number
	total = total + number
	count = count + 1

average = total / count
print("The sum of all numbers: ", total)
print("The average: ", average)
print("The lowest number is: ", min_number)
print("The highest number is: ", max_number)
