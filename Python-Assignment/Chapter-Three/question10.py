investment_amount = int(input("Enter investment amount: "))
annual_return = int(input("Enter annual return rate: "))
percentage_annual_return = annual_return / 100
added_percentage_annual_return = percentage_annual_return + 1

for no_of_years in range(1, 31):
	added_annual_return_power = pow(added_percentage_annual_return, no_of_years)
	product = investment_amount * added_annual_return_power
	print ("The investment amount after ", no_of_years, " years: ", product)