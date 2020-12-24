from random import random
import random
from django.shortcuts import render
import pandas as pd
from pages_app.models import OneBook
from pages_app.readFromFirebase import read_from_firebase

# d_frame = pd.read_csv("Assets/Data.csv")  # read from csv
d_frame = read_from_firebase()  # read from firebase API


def shuffle_dataframe():
    return d_frame.sample(frac=1)  # shuffles df


def group(books, bt):
    index = 0
    book_list = []
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
            book_obj.genres = df6.genres.values[index]
            book_obj.page_num = df6.page_num.values[index]
            book_obj.pub_year = df6.pub_year.values[index]
            book_obj.rating = df6.rating.values[index]
            book_obj.image_url = df6.image_url.values[index].lower()
            book_obj.isbn = df6.isbn.values[index]
            book_list.append(book_obj)
            index += 1

    return book_list


def group2(books, bt):
    gk = books.groupby('genres')
    df4 = gk.get_group(bt)
    df5 = df4.groupby('rating')
    max_rating = max(df5.rating)
    df6 = df5.get_group(max_rating[0])
    book_list = []
    for x in range(4):
        book_obj = OneBook()
        book_obj.title = df6.title.values[x]
        book_obj.writer = df6.writer.values[x]
        book_obj.genres = df6.genres.values[x]
        book_obj.page_num = df6.page_num.values[x]
        book_obj.pub_year = df6.pub_year.values[x]
        book_obj.rating = df6.rating.values[x]
        book_obj.image_url = df6.image_url.values[x].lower()
        book_obj.isbn = df6.isbn.values[x]
        book_list.append(book_obj)
    return book_list

    print("test")
# home page function renders index.html and returns response
def home(request):
    # books = BookClass.objects.all().order_by('-id')[:] # read from postgres
    # books = get_df()
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
        book_obj.genres = books.genres.values[temp]
        book_obj.page_num = books.page_num.values[temp]
        book_obj.pub_year = books.pub_year.values[temp]
        book_obj.rating = books.rating.values[temp]+1
        book_obj.image_url = books.image_url.values[temp].lower()
        book_obj.isbn = books.isbn.values[temp]
        book.append(book_obj)
    return render(request, 'pages/index.html', {'books': book})


# find out user choice and redirect to relevant page.
def user_choice(request):
    # books = get_df()
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
            book_obj.genres = books.genres.values[temp]
            book_obj.page_num = books.page_num.values[temp]
            book_obj.pub_year = books.pub_year.values[temp]
            book_obj.rating = books.rating.values[temp]+1
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
            book_obj.genres = books.genres.values[temp]
            book_obj.page_num = books.page_num.values[temp]
            book_obj.pub_year = books.pub_year.values[temp]
            book_obj.rating = books.rating.values[temp]+1
            book_obj.image_url = books.image_url.values[temp].lower()
            book_obj.isbn = books.isbn.values[temp]
            book.append(book_obj)
        return render(request, 'pages/not_inter_book.html', {'books': book})
    elif 'search' in request.POST:
        return render(request, 'pages/search.html')


# our user_chose page view
def result1(request):
    # books = get_df()
    df = shuffle_dataframe()  # shuffles df

    books = df

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
    books = books.loc[:, ["title", "writer", "genres", "page_num", "pub_year", "rating", "isbn", "image_url"]]
    books = books.applymap(lambda s: s.upper() if type(s) == str else s)
    book_types = []

    if bt == "NONE" and bt2 == "NONE" and bt3 == "NONE" and bt4 == "NONE" and bt5 == "NONE":
        return render(request, 'pages/NameError.html')
    book_types.append(bt)
    book_types.append(bt2)
    book_types.append(bt3)
    book_types.append(bt4)
    book_types.append(bt5)
    book = group(books, book_types)
    return render(request, 'pages/result.html', {'books': book})


def result2(request):
    # books = get_df()
    df = shuffle_dataframe()  # shuffles df

    books = d_frame
    books = books.loc[:, ["title", "writer", "isbn", "page_num", "pub_year", "rating", "image_url", "genres"]]
    books = books.applymap(lambda s: s.upper() if type(s) == str else s)
    if request.method == 'POST':
        selected_types = request.POST.getlist('ckb')
    if len(selected_types) < 3:
        return render(request, 'pages/selected_book_error.html')
    else:
        bt = selected_types[0].upper()
        bt2 = selected_types[1].upper()
        bt3 = selected_types[2].upper()

    book_list = []
    temp = group2(books, bt)
    book_list.append(temp[0])
    book_list.append(temp[1])
    book_list.append(temp[2])
    book_list.append(temp[3])

    temp = group2(books, bt2)
    book_list.append(temp[0])
    book_list.append(temp[1])
    book_list.append(temp[2])
    book_list.append(temp[3])

    temp = group2(books, bt3)
    book_list.append(temp[0])
    book_list.append(temp[1])
    book_list.append(temp[2])
    book_list.append(temp[3])
    return render(request, 'pages/result.html', {'books': book_list})


def search_result(request):
    if 'book_type' in request.POST:
        bt = request.POST['book_type'].upper()
    else:
        bt = ""
    if bt == "":
        return render(request, 'pages/search_error.html')
    else:
        # df = get_df()
        df = shuffle_dataframe()  # shuffles df

        book = []
        counter = 1
        for i in range(len(df)):
            if df.genres.values[i] == bt:
                book_obj = OneBook()
                book_obj.title = df.title.values[i]
                book_obj.writer = df.writer.values[i]
                book_obj.genres = df.genres.values[i]
                if book_obj.genres == "TEXTBOOK":
                    book_obj.genres = "ADVENTURE"
                book_obj.page_num = df.page_num.values[i]
                book_obj.pub_year = df.pub_year.values[i]
                book_obj.rating = df.rating.values[i]
                book_obj.image_url = df.image_url.values[i].lower()
                book_obj.isbn = df.isbn.values[i]
                book.append(book_obj)
                if counter == 20:
                    break
                counter += 1

        return render(request, 'pages/search_result.html', {'books': book})
