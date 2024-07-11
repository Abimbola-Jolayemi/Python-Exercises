grade = int(input("Enter your grade: "))

if grade >= 75 and grade <= 100:
	print("A")
elif grade >= 65 and grade < 75:
	print("B")
elif grade >= 50 and grade < 65:
	print("C")
elif grade >= 40 and grade < 50:
	print("D")
elif grade < 40:
	print("F")
else:
	print("Invalid grade")
 

total = 0
counter = 0
score = int(input("Enter score: "))
while score != -1:
	counter += 1
	total += score
	score = int(input("Enter score: "))

average = total / counter
print(average)