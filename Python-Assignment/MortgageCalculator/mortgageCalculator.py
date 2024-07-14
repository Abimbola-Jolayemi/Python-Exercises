principal = float(input("Enter the principal amount: "))

rate = int(input("Enter rate: "))

no_of_years = int(input("Enter number of years: "))

annual_rate = rate / 100 / 12

duration = no_of_years * 12

numerator = annual_rate * (1 + annual_rate) ** duration

denominator = ((1 + annual_rate) ** duration) - 1

monthly_payment = principal * (numerator / denominator)

print("Monthly payment: ", monthly_payment)