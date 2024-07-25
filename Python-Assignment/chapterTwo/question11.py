number = int(input("Enter a five-digit integer: "))

number5 = number % 10
number = number // 10

number4 = number % 10
number = number // 10

number3 = number % 10
number = number // 10

number2 = number % 10
number = number // 10

number1 = number % 10

print(number1, "   ", number2, "   ", number3, "   ", number4, "   ", number5)