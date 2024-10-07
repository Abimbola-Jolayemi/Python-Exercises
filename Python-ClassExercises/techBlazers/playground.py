def is_multiple_of_five(n):
    return n % 5 == 0

numbers = list(range(1, 101))
result = []
result = [number for number in numbers if number % 5 == 0]

print(result)

x = [[_ for _ in range(4)] for _ in range(5)]
print(x)

y = list(range(4))
x1 = []
for index in range(5):
    x1.append(y)
print(x1)

for index1 in range(5):
    for index2 in range(4):
        x[index1][index2] = index2

print(x)

score = (1, 2, 2, 3, 'bimbola')
print(type(score))
print(score.count(2))
print(score[4])