numbers = list(range(1,21))

even_numbers = []
for number in numbers:
	if number % 2 == 0:
		even_numbers.append(number)

print(even_numbers)

name = "fabulous"
result = ""
for index in range(len(name)-1):
	if index % 2 == 0:
		result += name[index]
print(result)

inner = [0] * 4

outer = []
for _ in range(5):
	outer.append(inner[:])

outer[1][0] = 10
print(outer)



		