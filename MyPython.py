even_total = 0
odd_total = 0

for index in range(1, 11):
	print(index)
	number = int(input("Enter any number: "))
	
	if number % 2 == 0:
		even_total += number
	else:
		odd_total += number

		

print("The sum of even numbers is: ", even_total)
print("The sum of odd numbers is: ", odd_total)

score = int(input(