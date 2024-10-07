import string
def switch_string(string1, string2):
    new_string1_array = []
    new_string2_array = []
    for index in string1:
        new_string1_array.append(index)
    for index in string2:
        new_string2_array.append(index)
    result = new_string2_array[0] + new_string2_array[1] + new_string1_array[2] + " " + new_string1_array[0] + new_string1_array[1] + new_string2_array[2]
    return result

print(switch_string("abc", "xyz"))

def add_ce(word, word2='ce'):
    even_length = len(word) // 2
    if len(word) % 2 == 0:
        first_slice = word[:even_length]
        second_slice = word[even_length:]
        word = first_slice + word2 + second_slice
    else:
        word += word2
    return word
print(add_ce("helloo", 'ce'))
print(add_ce("joy"))


def arrange_case(word):
    lower_case = ''
    upper_case = ''
    for character in word:
        if character == character.lower():
            lower_case += character
        else:
            upper_case += character
    new_word = upper_case + lower_case
    return new_word
print(arrange_case('sEmICoLOn'))

def get_character_occurence(word, character):
    count = 0
    for word_character in word:
        if word_character == character:
            count += 1
    return (character, count)
print(get_character_occurence("semicolon", 'o'))

def remove_punctuation(word):
    new_word = ''
    for character in word:
        if character.isalpha():
            new_word += character
    return new_word

print(remove_punctuation("he,ll.o"))