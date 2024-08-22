def savings_account(final_account_value, monthly_interest_rate, years):
	annual_interest_rate = (monthly_interest_rate / 100) / 12
	no_of_months = years * 12
	initial_deposit_amount = final_account_value / (1 + annual_interest_rate) ** no_of_months
	return initial_deposit_amount

print(savings_account(10000, 5, 10))