number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))
number3 = float(input("Enter a number: "))

if number1 > number2 and number1 > number3:
	print(number1, "is the highest")
elif number2 > number1 and number2 > number3:
	print(number2, "is the highest")
elif number3 > number1 and number3 > number2:
	print(number3, "is the highest")
else:
	pirnt("Invalid!!!")