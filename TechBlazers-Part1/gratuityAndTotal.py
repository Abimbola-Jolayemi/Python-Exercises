def gratuityAndTotal(subtotal, gratuity_rate):
	gratuity = (gratuity_rate / 100) * subtotal
	total = gratuity + subtotal
	return gratuity, total

print(gratuityAndTotal(10, 15))