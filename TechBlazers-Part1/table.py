def table():
	print(f"{"a":<5}{"b":<5}{"a**b"}")
	
	for number in range (1, 6):
		num = number + 1
		exponents = number ** num
		print(f"{number:<5}{num:<5}{exponents}")
	
table()

