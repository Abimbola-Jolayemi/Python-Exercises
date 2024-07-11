print("WELCOME TO COMFORT BANK")

accountBalance = 0

while True:
	decision = int(input('''
	1. Deposit
	2. Withdraw
	0. Exit
	Enter your choice: '''))
	if decision == 0:
		break

	if decision == 1:
		deposit = int(input("Enter amount to be deposited: "))
		accountBalance += deposit
		print(accountBalance)
	elif decision == 2:
		withdrawal = int(input("Enter amount to be withdrawn: "))
		if withdrawal <= accountBalance:
			accountBalance = accountBalance - withdrawal
			print(accountBalance)
		else:
			print("Insufficient funds")

	else:
		print("Invalid input, kindly select 0, 1 or 2")

print("Account Balance is: ", accountBalance)