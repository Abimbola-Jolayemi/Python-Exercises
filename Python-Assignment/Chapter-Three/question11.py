total_miles = 0
total_gallons = 0

miles_driven = int(input("Enter miles driven: "))

while miles_driven != -1:
	total_miles = total_miles + miles_driven

	gallons_used = float(input("Enter gallons used: "))
	total_gallons = total_gallons + gallons_used

	miles_per_gallons = miles_driven / gallons_used
	print("The miles per gallon for this week: ", miles_per_gallons)

	miles_driven = int(input("Enter miles driven: "))

combined_miles_per_gallons = total_miles / total_gallons

print("The combined miles per gallon: ", combined_miles_per_gallons)