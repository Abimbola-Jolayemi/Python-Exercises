factorial = 1

number = int(input("Enter any number: "))

for index in range(0, number):
	factorial = factorial * (number - index)

print("The factorial is:",factorial)