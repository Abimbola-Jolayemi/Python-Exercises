def get_length(name):
	"""Gets and return 
	the length of an iterable argument"""
	count = 0
	for index in name:
		count = count + 1
	return count

print(get_length([1,2,3,4,5]))