def fahrenheit(celsius):
    return (9 / 5) * celsius + 32


print(f"{'-' * 25}")
print(f"{'Celsius':<10} {'|' * 1}  {'Fahrenheit':<10}")
print()
    
for celsius in range(101):
        fahrenheit_temp = round(fahrenheit(celsius), 1)
        print(f"{celsius:<10} {'|' * 1} {fahrenheit_temp:<10}")

