from random import randint

lottery_number = randint(100, 999)
users_input = int(input("Enter a three-digit number: "))

lottery_digit1 = lottery_number % 10
lottery_number = lottery_number // 10

lottery_digit2 = lottery_number % 10
lottery_number = lottery_number // 10

lottery_digit3 = lottery_number

users_digit1 = users_input % 10
users_input = users_input // 10

users_digit2 = users_input % 10
users_input = users_input // 10

users_digit3 = users_input

if users_digit3 == lottery_digit3 and users_digit2 == lottery_digit2 and users_digit1 == lottery_digit1:
	print("Your award is $10,000")
elif (users_digit3 == lottery_digit3 or users_digit2 == lottery_digit2 or users_digit1 == lottery_digit1) and (users_digit2 == lottery_digit1 or users_digit2 == lottery_digit2 or users_digit2 == lottery_digit3) and (users_digit3 == lottery_digit1 or users_digit3 == lottery_digit2 or users_digit3 == lottery_digit3):
	print("Your award is $3,000")
elif (users_digit3 == lottery_digit3 or users_digit2 == lottery_digit2 or users_digit1 == lottery_digit1) or (users_digit2 == lottery_digit1 or users_digit2 == lottery_digit2 or users_digit2 == lottery_digit3) or (users_digit3 == lottery_digit1 or users_digit3 == lottery_digit2 or users_digit3 == lottery_digit3):
	print("Your input matches one digit in the lottery number, your award is $0")
else:
	print("Sorry!!!, your input do not match the lottery number. Try again next time")