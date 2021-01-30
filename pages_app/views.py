import random
from random import random
import random
from django.shortcuts import render
import pandas as pd

from Assets import knn_logic
from pages_app.models import OneBook
from pages_app.readFromFirebase import read_from_firebase
import pages_app.convert_gen as convert_gen
# d_frame = pd.read_csv("Assets/yeah_bro.csv",sep=';')  # read from csv
d_frame = read_from_firebase()  # read from firebase API


def shuffle_dataframe():
    return pd.concat([d_frame[:1], d_frame[1:].sample(frac=1)]).reset_index(drop=True)


def group(books, bt):
    index = 0
    book_list = []
    try:
        for book_type in bt:
            if book_type != "NONE":
                gk = books.groupby('genres')
                df4 = gk.get_group(book_type)
                df5 = df4.groupby('rating')
                max_rating = max(df5.rating)
                df6 = df5.get_group(max_rating[0])
                book_obj = OneBook()
                book_obj.title = df6.title.values[index]
                book_obj.writer = df6.writer.values[index]
                book_obj.genres = convert_gen.convert_genres1(df6.genres.values[index])
                book_obj.page_num = df6.page_num.values[index] + 150
                book_obj.pub_year = df6.pub_year.values[index]
                book_obj.rating = df6.rating.values[index]
                book_obj.image_url = df6.image_url.values[index].lower()
                book_obj.isbn = df6.isbn.values[index]
                book_list.append(book_obj)
                index += 1
    except IndexError:
        # books = get_df()
        df = shuffle_dataframe()  # shuffles df
        my_books = df
        book = []
        tempo = []
        for i in range(4):
            flag = False
            while not flag:
                rand_num = list(range(len(my_books)))
                random.shuffle(rand_num)
                temp = rand_num.pop()
                if my_books.rating.values[temp] == 4 and my_books.book_id.values[temp] \
                        not in tempo and not "NOPHOTO" in str(my_books.image_url[temp]):
                    flag = True

            book_obj = OneBook()
            book_obj.title = my_books.title.values[temp]
            book_obj.writer = my_books.writer.values[temp]
            book_obj.genres = convert_gen.convert_genres1(my_books.genres.values[temp])
            book_obj.page_num = my_books.page_num.values[temp] + 150
            book_obj.pub_year = my_books.pub_year.values[temp]
            book_obj.rating = my_books.rating.values[temp] + 1
            book_obj.image_url = my_books.image_url.values[temp].lower()
            book_obj.isbn = my_books.isbn.values[temp]
            book.append(book_obj)
            return book
    return book_list


def group2(books, bt):
    book_list = []
    try:
        gk = books.groupby('genres')
        df4 = gk.get_group(bt)
        df5 = df4.groupby('rating')
        max_rating = max(df5.rating)
        df6 = df5.get_group(max_rating[0])
        for x in range(4):
            book_obj = OneBook()
            book_obj.title = df6.title.values[x]
            book_obj.writer = df6.writer.values[x]
            book_obj.genres = convert_gen.convert_genres1(df6.genres.values[x])
            book_obj.page_num = df6.page_num.values[x] + 150
            book_obj.pub_year = df6.pub_year.values[x]
            book_obj.rating = df6.rating.values[x]
            book_obj.image_url = df6.image_url.values[x].lower()
            book_obj.isbn = df6.isbn.values[x]
            book_list.append(book_obj)
    except IndexError:
        # books = get_df()
        df = shuffle_dataframe()  # shuffles df

        my_books = df
        book = []
        tempo = []
        for i in range(4):
            flag = False
            while not flag:
                rand_num = list(range(len(my_books)))
                random.shuffle(rand_num)
                temp = rand_num.pop()
                if my_books.rating.values[temp] == 4 and my_books.book_id.values[temp] \
                        not in tempo and not "NOPHOTO" in str(my_books.image_url[temp]):
                    flag = True

            book_obj = OneBook()
            book_obj.title = my_books.title.values[temp]
            book_obj.writer = my_books.writer.values[temp]
            book_obj.genres = convert_gen.convert_genres1(my_books.genres.values[temp])
            book_obj.page_num = my_books.page_num.values[temp] + 150
            book_obj.pub_year = my_books.pub_year.values[temp]
            book_obj.rating = my_books.rating.values[temp] + 1
            book_obj.image_url = my_books.image_url.values[temp].lower()
            book_obj.isbn = my_books.isbn.values[temp]
            book.append(book_obj)
            return book
    return book_list


# home page function renders index.html and returns response
def home(request):
    df = shuffle_dataframe()
    books = df
    book = []
    tempo = []
    for i in range(6):
        flag = False
        while not flag:
            rand_num = list(range(len(books)))
            random.shuffle(rand_num)
            temp = rand_num.pop()
            if books.rating.values[temp] == 4 and books.book_id.values[temp] not in tempo and not "NOPHOTO" in str(
                    books.image_url[temp]):
                flag = True
            tempo.append(books.book_id.values[temp])
        book_obj = OneBook()
        book_obj.title = books.title.values[temp]
        book_obj.writer = books.writer.values[temp]
        book_obj.genres = convert_gen.convert_genres1(books.genres.values[temp])
        book_obj.page_num = books.page_num.values[temp] + 150
        book_obj.pub_year = books.pub_year.values[temp]
        book_obj.rating = books.rating.values[temp] + 1
        book_obj.image_url = books.image_url.values[temp].lower()
        book_obj.isbn = books.isbn.values[temp]
        book.append(book_obj)
    return render(request, 'pages/index.html', {'books': book})


# find out user choice and redirect to relevant page.
def user_choice(request):
    df = shuffle_dataframe()  # shuffles df
    books = df
    book = []
    tempo = []
    if 'yes_enter' in request.POST:
        for i in range(6):
            flag = False
            while not flag:
                rand_num = list(range(len(books)))
                random.shuffle(rand_num)
                temp = rand_num.pop()
                if books.rating.values[temp] == 4 and books.book_id.values[temp] not in tempo and not "NOPHOTO" in str(
                        books.image_url[temp]):
                    flag = True
            book_obj = OneBook()
            book_obj.title = books.title.values[temp]
            book_obj.writer = books.writer.values[temp]
            book_obj.genres = convert_gen.convert_genres1(books.genres.values[temp])
            book_obj.page_num = books.page_num.values[temp] + 150
            book_obj.pub_year = books.pub_year.values[temp]
            book_obj.rating = books.rating.values[temp] + 1
            book_obj.image_url = books.image_url.values[temp].lower()
            book_obj.isbn = books.isbn.values[temp]
            book.append(book_obj)
        return render(request, 'pages/inter_book.html', {'books': book})
    elif 'no_enter' in request.POST:
        for i in range(6):
            flag = False
            while not flag:
                rand_num = list(range(len(books)))
                random.shuffle(rand_num)
                temp = rand_num.pop()
                if books.rating.values[temp] == 4 and books.book_id.values[temp] not in tempo and not "NOPHOTO" in str(
                        books.image_url[temp]):
                    flag = True
            book_obj = OneBook()
            book_obj.title = books.title.values[temp]
            book_obj.writer = books.writer.values[temp]
            book_obj.genres = convert_gen.convert_genres1(books.genres.values[temp])
            book_obj.page_num = books.page_num.values[temp] + 150
            book_obj.pub_year = books.pub_year.values[temp]
            book_obj.rating = books.rating.values[temp] + 1
            book_obj.image_url = books.image_url.values[temp].lower()
            book_obj.isbn = books.isbn.values[temp]
            book.append(book_obj)
        return render(request, 'pages/not_inter_book.html', {'books': book})
    elif 'search' in request.POST:
        return render(request, 'pages/search.html')


# our user_chose page view
def result1(request):
    df = d_frame
    if 'book1_type' in request.POST:
        bt = request.POST['book1_type'].upper()
    else:
        bt = ""
    if 'book1_type' in request.POST:
        bt2 = request.POST['book2_type'].upper()
    else:
        bt2 = ""
    if 'book3_type' in request.POST:
        bt3 = request.POST['book3_type'].upper()
    else:
        bt3 = ""
    if 'book4_type' in request.POST:
        bt4 = request.POST['book4_type'].upper()
    else:
        bt4 = ""
    if 'book5_type' in request.POST:
        bt5 = request.POST['book5_type'].upper()
    else:
        bt5 = ""
    if bt == "NONE" and bt2 == "NONE" and bt3 == "NONE" and bt4 == "NONE" and bt5 == "NONE":
        return render(request, 'pages/NameError.html')

        # *********************************************************
        # books = df
        # books = books.loc[:, ["title", "writer", "genres", "page_num", "pub_year", "rating", "isbn", "image_url"]]
        # books = books.applymap(lambda s: s.upper() if type(s) == str else s)
        # book_types = [bt, bt2, bt3, bt4, bt5]
        # book = group(books, book_types)
        # *********************************************************

    book_types_list = [bt, bt2, bt3, bt4, bt5]
    temp_book_types_list = []
    for i in range(len(book_types_list)):
        if book_types_list[i] != "NONE":
            temp_book_types_list.append(book_types_list[i])
    type_int_list = convert_gen.convert_genres(temp_book_types_list)

    book = []
    b_list = []
    i = 0
    while i in range(len(type_int_list)):
        one_book = knn_logic.ml_logic(df, type_int_list[i])
        if one_book.isbn not in b_list:
            book.append(one_book)
            b_list.append(one_book.isbn)
        else:
            if i != 0:
                i -= 1
        i += 1
    return render(request, 'pages/result.html', {'books': book})


def result2(request):
    df = d_frame
    # books = df
    # books = books.loc[:, ["title", "writer", "isbn", "page_num", "pub_year", "rating", "image_url", "genres"]]
    # books = books.applymap(lambda s: s.upper() if type(s) == str else s)
    if request.method == 'POST':
        selected_types = request.POST.getlist('ckb')
    if len(selected_types) < 3:
        return render(request, 'pages/selected_book_error.html')
    else:
        bt = selected_types[0].upper()
        bt2 = selected_types[1].upper()
        bt3 = selected_types[2].upper()

    # book_list = []
    # temp = group2(books, bt)
    # for i in range(len(temp)):
    #     book_list.append(temp[i])
    #
    # temp = group2(books, bt2)
    # for i in range(len(temp)):
    #     book_list.append(temp[i])
    #
    # temp = group2(books, bt3)
    # for i in range(len(temp)):
    #     book_list.append(temp[i])

    temp_book_types_list = [bt, bt2, bt3]
    type_int_list = convert_gen.convert_genres(temp_book_types_list)
    b_list = []
    book_list = []
    for ind in range(3):
        i = 0
        while i in range(4):
            one_book = knn_logic.ml_logic(df, type_int_list[ind])
            if one_book.isbn not in b_list:
                book_list.append(one_book)
                b_list.append(one_book.isbn)
            else:
                if i != 0:
                    i -= 1
            i += 1
    return render(request, 'pages/result.html', {'books': book_list})


def search_result(request):
    if 'book_type' in request.POST:
        bt = request.POST['book_type'].upper()
    else:
        bt = ""
    if bt == "":
        return render(request, 'pages/search_error.html')
    else:
        df = shuffle_dataframe()  # shuffles df
        temp_bt = [bt]
        temp_bt = convert_gen.convert_genres(temp_bt)
        book = []
        counter = 1
        for i in range(len(df)):
            if df.genres.values[i] == temp_bt[0]:
                book_obj = OneBook()
                book_obj.title = df.title.values[i]
                book_obj.writer = df.writer.values[i]
                book_obj.genres = convert_gen.convert_genres1(df.genres.values[i])
                book_obj.page_num = df.page_num.values[i] + 150
                book_obj.pub_year = df.pub_year.values[i]
                book_obj.rating = 5
                book_obj.image_url = df.image_url.values[i].lower()
                book_obj.isbn = df.isbn.values[i]
                book.append(book_obj)
                if counter == 20:
                    break
                counter += 1
        return render(request, 'pages/search_result.html', {'books': book})
