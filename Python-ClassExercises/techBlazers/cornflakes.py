from operator import truediv


#def biggest_odd(numbers):
    #max_number = 0
    #if len(numbers) > 1 and int(numbers) > 0:
        #for character in numbers:
            #integer = int(character)
            #if integer > max_number and integer % 2 == 1:
            #    max_number = integer
   # return max_number

#def equal_strings(string1, string2):
    #if len(string1) == len(string2) and set(string1) == set(string2):
       # return "True"
    #else:
       # return "False"

def get_key_cube(list_of_numbers):
    numbers_cube = {}
    for number in list_of_numbers:
        numbers_cube[number] = number ** 3
    return numbers_cube

    # OR

def get_key_cube1(list_of_numbers):
    return {number: number ** 3 for number in list_of_numbers}



numbers_list = [1,2,3,4,5]
dict_numbers = get_key_cube(numbers_list)
dict_numbers2 = get_key_cube1(numbers_list)
print(dict_numbers)
print(dict_numbers2)


