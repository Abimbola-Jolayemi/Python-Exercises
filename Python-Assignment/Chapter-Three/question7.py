print(f"{"Number":<10}{"Square":<10}{"Cube":<10}")

for index in range(0, 6):
	index_squared = index * index
	index_cubed = index * index * index

	print(f"{index:>6}{index_squared:>9}{index_cubed:>9}")