
def return_dict(words):
    if not isinstance(words, str):
        raise TypeError("Invalid input")
    word_in_lower_case = words.lower()
    my_dict = {}
    for character in word_in_lower_case:
        if character in my_dict:
            my_dict[character] += 1
        else:
            my_dict[character] = 1
    return my_dict

print(return_dict("abimbolajolayemi"))
print(return_dict("Abimbola"))
