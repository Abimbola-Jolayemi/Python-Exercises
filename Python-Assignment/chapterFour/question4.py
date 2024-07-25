def mystery(x):
	 y = 0
	 for value in x:
	 	y += value ** 2
	 return y

print(mystery([1, 2, 3, 4, 5]))

#The mystery function takes in any iterable consisting of numbers (x) as an argument and returns the sum of the squares of its elements.