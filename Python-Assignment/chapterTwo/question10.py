number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

sum = number1 + number2 + number3

average = sum / 3

product = number1 * number2 * number3

if number1 > number2 and number1 > number3:
	print(number1, "is the largest")
elif number2 > number1 and number2 > number3:
	print(number2, "is the largest")
elif number3 > number1 and number3 > number2:
	print(number3, "is the largest")
else:
	print("All numbers are equal")