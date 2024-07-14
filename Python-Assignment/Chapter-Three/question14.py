pi = 0.00
no_of_terms = 0


print(f"{"Terms":<10}{"Approximation":<10}")

for index in range(400):
	if index % 2 == 0:
		term = (4.0 * 1) / (2 * index + 1)
	else:
		term = (4.0 * -1) / (2 * index + 1)

	pi = pi + term
	no_of_terms = no_of_terms + 1

	print(f"{no_of_terms:<10}{pi:<10}")

	
