binary_number = int(input("Enter a binary_number: "))

decimal_number = 0
count = 1

while binary_number > 0:
	digit = binary_number % 10

	decimal_number += digit * count

	count = count * 2

	binary_number = binary_number // 10

print(decimal_number)