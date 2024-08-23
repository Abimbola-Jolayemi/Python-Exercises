def add_string(numbers):
	total = 0
	for number in numbers:
		total += int(number)
	return str(total)

print(add_string("123"))