def addUpDigits(number):
	total = 0
	while number > 0:
		digit = number % 10
		total = total + digit
		number = number // 10
	return total
		
print(addUpDigits(932))