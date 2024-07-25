price_of_car = int(input("Enter Price of your car: "))

if price_of_car <= 1000000:
	road_tax = (10 / 100) * price_of_car
	print(f"The road tax is: {road_tax}")
elif price_of_car > 1000000 and price_of_car <= 3000000:
	road_tax = (15 / 100) * price_of_car
	print(f"The road tax is: {road_tax}") 
elif price_of_car > 3000000 and price_of_car <= 5000000:
	road_tax = (20 / 100) * price_of_car
	print(f"The road tax is: {road_tax}")
elif price_of_car > 5000000:
	road_tax = (25 / 100) * price_of_car
	print(f"The road tax is: {road_tax}")