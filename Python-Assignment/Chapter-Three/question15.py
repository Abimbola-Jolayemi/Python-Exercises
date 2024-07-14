constant_e = 0.00

for term in range(0, 10):
	factorial = 1
	for index in range (1, term):
		factorial *= (term - index)
	constant_e += 1.0 / factorial

print("The estimated value for constant e using 10 terms is:", constant_e)