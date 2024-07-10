investment_amount = int(input("Enter the original investment amount: "))
annual_interest_rate = int(input("Enter the annual interest rate: "))
no_of_years = int(input("Enter number of years: "))

percentage_interest_rate = annual_interest_rate / 100

percentageInterestRate_plusOne = percentage_interest_rate + 1

percentageInterestRatePlusOne_exponentNoOfYears = percentageInterestRate_plusOne ** no_of_years

investment_return = investment_amount * percentageInterestRatePlusOne_exponentNoOfYears

print(investment_return)