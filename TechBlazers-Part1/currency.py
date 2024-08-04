conversion_choice = int(input("Enter 0 (USD to naira) or 1 (naira to USD): "))
amount = int(input("Enter amount to be converted: "))

if conversion_choice == 0:
	print(f"Amount in naira: #{amount * 1500}")
elif conversion_choice == 1:
	print(f"Amount in Dollars: ${amount // 1500}")
else:
	print("Enter a valid input!!!")