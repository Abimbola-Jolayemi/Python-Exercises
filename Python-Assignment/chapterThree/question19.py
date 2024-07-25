max_number = 20

for side1 in range(1, max_number+1):
	for side2 in range(side1, max_number+1):
		for side3 in range(side2, max_number+1):
			if (side1 ** 2) + (side2 ** 2) == side3 ** 2:
				print(f"{side1}, {side2}, {side3}")