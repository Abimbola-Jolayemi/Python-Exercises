print("Enter two integers and I will show you the relationship between the two integers")

number1 = int(input("Integer 1 : "))
number2 = int(input("Integer 2 : "))

if number1 == number2:
	print(number1, "is equal to", number2)
else:
	print(number1, "is not equal to", number2)

if number1 > number2:
	print(number1, "is greater than", number2)
else:
	print(number1, "is not greater than", number2)

if number1 < number2:
	print(number1, "is less than", number2)
else:
	print(number1, "is not less than", number2)