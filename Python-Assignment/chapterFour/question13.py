def product(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


print(product(1, 2, 3))
print(product(1, 2, 3, 4))
print(product(1, 2, 3, 4, 5))
print(product(1, 2, 3, 4, 5, 6))
print(product())
