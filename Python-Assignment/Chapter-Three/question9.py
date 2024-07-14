number = int(input("Enter a five-digit integer: "))

for index in range(0, 5):
	digit = int(number % 10)

	number = number / 10
	print(digit , end=' ')
