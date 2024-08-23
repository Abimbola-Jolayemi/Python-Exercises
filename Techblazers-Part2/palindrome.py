def reverse(number):
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return reversed_number

def palindrome(number):
	if reverse(number) == number:
		return True
	else:
		return False

print(reverse(456))
print(palindrome(456))