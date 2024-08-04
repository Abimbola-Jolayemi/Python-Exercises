def add_up_digits(number):
	total = 0
	while number > 0:
		digit = number % 10
		total = total + digit
		number = number // 10
	return total
		
print(add_up_digits(932))