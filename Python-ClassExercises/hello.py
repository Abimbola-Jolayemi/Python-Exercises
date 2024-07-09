print('Hello World!!!')
print("How do you do? ") 

print('')

n = 10
m = 12
x = n + m
print (x)

print('')

print(type(5.6))

print('')

name = 'Timothy'
age = 56

print(f'{name} \n {age}')

print('')

name_input = input("Enter your name: ")
age_input = input("Indicate your age pls!!!: ")
age_input = int(age_input)

print ("Your details are: ", name_input, age_input)

print('')

password = input("Enter password: ")
noOfCharacters = len(password)

print ('*' * noOfCharacters)

print('')

firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
age = input("Enter age: ")

print("Your full name is", firstName, lastName, ", and your age is", age)

print('')

message = '''	My name is Abimbola Jolayemi
	I love Chidinma, Dunni and Adenike
	I love my Cohort female mates'''

print (message)

print('')

message1 = ' My name is Abimbola Jolayemi \n I love Chidinma, Dunni and Adenike \n I love my Cohort female mates'

print (message1)

print('')

new_name = input("enter your name: ")
new_age = int(input("enter new age: "))

if new_age >= 20 and new_age <= 45:
	print('your name is ', new_name)
	print('You eligible to apply')
	print('Proceed to enter details: ')
elif new_age >= 13 and new_age <= 19:
	print('You are still a teeneager')
else:
	print("Kindly log-out as you're ineligible")

print('')

print("End of Application")
print("Thank You!!!")
