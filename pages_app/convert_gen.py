def convert_genres(temp_book_types_list):
    type_int_list = []
    for i in range(len(temp_book_types_list)):
        if temp_book_types_list[i] == "SCIENCEFICTION":
            type_int_list.append(0)
        elif temp_book_types_list[i] == "CLASSIC":
            type_int_list.append(1)
        elif temp_book_types_list[i] == "PHILOSOPHY":
            type_int_list.append(2)
        elif temp_book_types_list[i] == "BIOGRAPHY":
            type_int_list.append(3)
        elif temp_book_types_list[i] == "YOUNGADULT":
            type_int_list.append(4)
        elif temp_book_types_list[i] == "TRAVEL":
            type_int_list.append(5)
        elif temp_book_types_list[i] == "CRIME":
            type_int_list.append(6)
        elif temp_book_types_list[i] == "SCIENCE":
            type_int_list.append(7)
        elif temp_book_types_list[i] == "HORROR":
            type_int_list.append(8)
        elif temp_book_types_list[i] == "HISTORY":
            type_int_list.append(9)
        elif temp_book_types_list[i] == "ADVENTURE":
            type_int_list.append(10)
    return type_int_list
