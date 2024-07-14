number = int(input("Enter a number: "))

for index in range(1, 13):
	product = number * index
	print(f"{number}{" * "}{index}{" = "}{product}")