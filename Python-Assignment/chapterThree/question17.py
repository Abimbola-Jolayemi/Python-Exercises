for outer_loop in range(0, 10):
	for inner_loop in range(0, outer_loop+1):
		print('*', end='')
	print()

print()

for outer_loop in range(0, 10):
	for inner_loop in range(0, 10-outer_loop):
		print('*', end='')
	print()

print()

for outer_loop in range(10):
	for space_loop in range(0, outer_loop):
		print(' ', end='')
	for inner_loop in range(0, 10-outer_loop):
		print('*',end='')
	print()

print()

for outer_loop in range(10):
	for space_loop in range(0, 10-outer_loop):
		print(' ', end='')
	for inner_loop in range(0, outer_loop+1):
		print('*',end='')
	print()

