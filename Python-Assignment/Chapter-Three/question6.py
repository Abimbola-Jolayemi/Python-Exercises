print(input("What is your problem?: "))

question = str(input("Have you had this problem before? (Yes or No): "))

match question:
	case 'Yes':
		print('Well, you have it again')
	case 'No':
		print('Well, you have it now')
	case _:
		print('Kindly select a valid option next time')
	