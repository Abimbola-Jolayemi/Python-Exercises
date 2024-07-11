number = int(input("Enter a number: "))

if number <= 0:
	print(number, " is an invalid")
elif number % 2 == 0:
	print(number, " is an even number")
elif number % 2 == 1:
	print(number, " is an odd number")