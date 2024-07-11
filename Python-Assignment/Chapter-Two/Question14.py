age = int(input("Enter age: "))

max_heart_rate = 220 - age

lower_range = 50 / 100
upper_range = 85 / 100

lowest_target_heart_rate = max_heart_rate * lower_range
highest_target_heart_rate = max_heart_rate * upper_range

print(f"The maximum heart rate is: {max_heart_rate} beats.")
print(f"The range of the heart rate is from {lowest_target_heart_rate} beats to {highest_target_heart_rate} beats.")