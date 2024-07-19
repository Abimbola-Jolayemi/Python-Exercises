words = input("Enter any word: ")
vowels = 0
consonants = 0
unique_vowels = ""
unique_consonants = ""

for character in words:
	if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
		if character not in unique_vowels:
			unique_vowels += character
			vowels = vowels + 1
	else:
		if character not in unique_consonants:
			unique_consonants += character
			consonants = consonants + 1

print(f"In the word {words}, we have {vowels} vowels and {consonants} consonants.")