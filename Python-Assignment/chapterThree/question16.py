largest = 0
second_largest = 0

for index in range(0, 10):
	number = int(input("Enter a number: "))

	if number > largest:
		second_largest = largest
		largest = number
	
	elif number > second_largest and number != largest:
		second_largest = number

print("The largest number is: ", largest)
print("The second largest number is: ", second_largest)