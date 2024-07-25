number = int(input("Enter any five-digit number: "))

digit1 = number % 10
number = number // 10

digit2 = number % 10
number = number // 10

digit3 = number % 10
number = number // 10

digit4 = number % 10
number = number // 10

digit5 = number % 10

if digit1 == digit5 and digit2 == digit4:
	print("Number is a Palindrome")
else:
	print("Number is not a Palindrome")