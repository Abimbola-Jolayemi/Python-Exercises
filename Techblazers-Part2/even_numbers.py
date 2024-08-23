list_of_even_digit_numbers = []
for number in range(1000, 3001):
    num_str = str(number)
    for digit in num_str:
        if int(digit) % 2 != 0:
            break
    else:
        list_of_even_digit_numbers.append(number)

print(list_of_even_digit_numbers)