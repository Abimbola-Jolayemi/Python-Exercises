def get_length(name):
	count = 0
	for index in name:
		count = count + 1
	return count

print(get_length([1,2,3,4,5]))