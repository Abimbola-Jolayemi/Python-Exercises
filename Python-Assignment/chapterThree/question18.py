for outer_loop in range(10):
	
	for inner_loop in range(outer_loop + 1):
		print('*', end='')
	for space_loop in range(10 - outer_loop - 1):
		print(' ', end='')
	print('   ', end='')


	for inner_loop in range(10 - outer_loop):
		print('*', end='')
	for space_loop in range(outer_loop):
		print(' ',end='')
	print('   ', end='')

	for space_loop in range(outer_loop):
		print(' ',end='')
	for inner_loop in range(10 - outer_loop):
		print('*', end='')
	print('   ', end='')

	
	for space_loop in range(10 - outer_loop - 1):
		print(' ',end='')
	for inner_loop in range(outer_loop + 1):
		print('*', end='')

	print()
	