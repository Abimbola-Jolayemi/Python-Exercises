def num_in_increasing_order(num1, num2, num3):
	if num1 > num2:
		num1, num2 = num2, num1
	if num1 > num3:
		num1, num3 = num3, num1
	if num2 > num3:
		num2, num3 = num3, num2
	return num1, num2, num3

print(num_in_increasing_order(2, 5, 1))
		