def my_discount(price, discount):
	if discount > 0 and discount <= 100:
		discounted_amount = (discount / 100) * price
		final_price = price - discounted_amount
		return final_price