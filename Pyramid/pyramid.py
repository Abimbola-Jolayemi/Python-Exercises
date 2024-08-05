number = input('Enter the number of lines: ')
height = int(number)

for i in range(1, height + 1):
  for j in range(height - i):
    print(' ', end='')
  for j in range(i,0, -1):
    print(j, end='')
  for j in range(2, i + 1):
    print(j, end='')
  print()