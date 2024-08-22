def gratuity_and_total(subtotal, gratuity_rate):
	gratuity = (gratuity_rate / 100) * subtotal
	total = gratuity + subtotal
	return gratuity, total

print(gratuity_and_total(10, 15))