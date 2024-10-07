
tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))
first_tuple = tuple(tuple2[1])
first_number = first_tuple[1]
first_index = first_tuple.index(20)

second_tuple = tuple2[2]
second_number = second_tuple[2]
second_index = second_tuple.index(25)

final_tuple = ((first_index, first_number), (second_index, second_number))
print(final_tuple)
