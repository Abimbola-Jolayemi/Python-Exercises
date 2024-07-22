print("0 for single, " "\n1 for married filing jointly" "\n2 for married filing separately" "\n3 for Head of Household")

print()
filing_status = int(input("Enter your filing status: "))
taxable_income = float(input("Enter your taxable income: "))

if filing_status == 0:
	if taxable_income >= 0 and taxable_income <= 8350:
		tax = 0.1 * taxable_income
	elif taxable_income >= 8351 and taxable_income <= 33950:
		tax = 0.15 * taxable_income
	elif taxable_income >= 33951 and taxable_income <= 82250:
		tax = 0.25 * taxable_income
	elif taxable_income >= 82251 and taxable_income <= 171550:
		tax = 0.28 * taxable_income
	elif taxable_income >= 171551 and taxable_income <= 372950:
		tax = 0.33 * taxable_income
	elif taxable_income >= 372951:
		tax = 0.35 * taxable_income

if filing_status == 1:
	if taxable_income >= 0 and taxable_income <= 16700:
		tax = 0.1 * taxable_income
	elif taxable_income >= 16701 and taxable_income <= 67900:
		tax = 0.15 * taxable_income
	elif taxable_income >= 67901 and taxable_income <= 137050:
		tax = 0.25 * taxable_income
	elif taxable_income >= 137051 and taxable_income <= 208850:
		tax = 0.28 * taxable_income
	elif taxable_income >= 208851 and taxable_income <= 372950:
		tax = 0.33 * taxable_income
	elif taxable_income >= 372951:
		tax = 0.35 * taxable_income

if filing_status == 2:
	if taxable_income >= 0 and taxable_income <= 8350:
		tax = 0.1 * taxable_income
	elif taxable_income >= 8351 and taxable_income <= 33950:
		tax = 0.15 * taxable_income
	elif taxable_income >= 33951 and taxable_income <= 68525:
		tax = 0.25 * taxable_income
	elif taxable_income >= 68526 and taxable_income <= 104425:
		tax = 0.28 * taxable_income
	elif taxable_income >= 104426 and taxable_income <= 186475:
		tax = 0.33 * taxable_income
	elif taxable_income >= 186476:
		tax = 0.35 * taxable_income

if filing_status == 3:
	if taxable_income >= 0 and taxable_income <= 11950:
		tax = 0.1 * taxable_income
	elif taxable_income >= 11951 and taxable_income <= 45500:
		tax = 0.15 * taxable_income
	elif taxable_income >= 45501 and taxable_income <= 117450:
		tax = 0.25 * taxable_income
	elif taxable_income >= 117451 and taxable_income <= 190200:
		tax = 0.28 * taxable_income
	elif taxable_income >= 190201 and taxable_income <= 372950:
		tax = 0.33 * taxable_income
	elif taxable_income >= 372951:
		tax = 0.35 * taxable_income

print(f"Your tax is: {tax:.2f}")
	