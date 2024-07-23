print("0 for single, " "\n1 for married filing jointly" "\n2 for married filing separately" "\n3 for Head of Household")

print()
filing_status = int(input("Enter your filing status: "))
taxable_income = float(input("Enter your taxable income: "))

if filing_status == 0:
		first_taxable = 8350
		second_taxable = taxable_income - first_taxable

		tax1 = 0.1 * 8350

		if taxable_income >= 8351 and taxable_income <= 33950:
			tax1 = tax1 + (0.15 * second_taxable)
		elif taxable_income >= 33951 and taxable_income <= 82250:
			tax1 = tax1 + (0.25 * second_taxable)
		elif taxable_income >= 82251 and taxable_income <= 171550:
			tax1 = tax1 + (0.28 * second_taxable)
		elif taxable_income >= 171551 and taxable_income <= 372950:
			tax1 = tax1 + (0.33 * second_taxable)
		elif taxable_income >= 372951:
			tax1 = tax1 + (0.35 * second_taxable)


elif filing_status == 1:
		first_taxable = 16700
		second_taxable = taxable_income - first_taxable

		tax1 = 0.1 * 16700

		if taxable_income >= 16701 and taxable_income <= 67900:
			tax1 = tax1 + (0.15 * second_taxable)
		elif taxable_income >= 67901 and taxable_income <= 137050:
			tax1 = tax1 + (0.25 * second_taxable)
		elif taxable_income >= 137051 and taxable_income <= 208850:
			tax1 = tax1 + (0.28 * second_taxable)
		elif taxable_income >= 208851 and taxable_income <= 372950:
			tax1 = tax1 + (0.33 * second_taxable)
		elif taxable_income >= 372951:
			tax1 = tax1 + (0.35 * second_taxable)
		

elif filing_status == 2:
		first_taxable = 8350
		second_taxable = taxable_income - first_taxable

		tax1 = 0.1 * 8350

		if taxable_income >= 8351 and taxable_income <= 33950:
			tax1 = tax1 + (0.15 * second_taxable)
		elif taxable_income >= 33951 and taxable_income <= 68525:
			tax1 = tax1 + (0.25 * second_taxable)
		elif taxable_income >= 68526 and taxable_income <= 104425:
			tax1 = tax1 + (0.28 * second_taxable)
		elif taxable_income >= 104426 and taxable_income <= 186475:
			tax1 = tax1 + (0.33 * second_taxable)
		elif taxable_income >= 186476:
			tax1 = tax1 + (0.35 * second_taxable)


elif filing_status == 3:
		first_taxable = 11950
		second_taxable = taxable_income - first_taxable

		tax1 = 0.1 * 11950

		if taxable_income >= 11951 and taxable_income <= 45500:
			tax1 = tax1 + (0.15 * second_taxable)
		elif taxable_income >= 45501 and taxable_income <= 117450:
			tax1 = tax1 + (0.25 * second_taxable)
		elif taxable_income >= 117451 and taxable_income <= 190200:
			tax1 = tax1 + (0.28 * second_taxable)
		elif taxable_income >= 190201 and taxable_income <= 372950:
			tax1 = tax1 + (0.33 * second_taxable)
		elif taxable_income >= 372951:
			tax1 = tax1 + (0.35 * second_taxable)


print(f"Your tax is: {tax1:.2f}")
	