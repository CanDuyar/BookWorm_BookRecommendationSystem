from django.shortcuts import render
import pandas as pd
import numpy as np
import random
from pages_app.models import BookClass, OneBook


# group function used in >>>>
def group(books, bt, index):
    if bt != "NONE":
        gk = books.groupby('Genres')
        df4 = gk.get_group(bt)

        df5 = df4.groupby('average_rating')

        max_rating = max(df5.average_rating)

        df6 = df5.get_group(max_rating[0])

        dico = {'title': df6.title.values[index], 'authors': df6.authors.values[index],
                'genres': df6.Genres.values[index], 'page_num': df6.books_count.values[index],
                'pub_year': df6.original_publication_year.values[index], 'rating': df6.average_rating.values[index],
                'image_url': df6.image_url.values[index], 'isbn': df6.isbn.values[index]}
        return dico
        # our home page view


def group2(books, bt):
    if bt != "NONE":
        gk = books.groupby('Genres')
        df4 = gk.get_group(bt)

        df5 = df4.groupby('average_rating')

        max_rating = max(df5.average_rating)

        df6 = df5.get_group(max_rating[0])

        for x in range(5):
            print(df6.title.values[x])
            print(df6.authors.values[x])
            print(df6.Genres.values[x])
            print(df6.books_count.values[x])
            print(df6.original_publication_year.values[x])
            print(df6.average_rating.values[x])
            print(df6.isbn.values[x])
            print("\n")


# home page function renders index.html and returns response
def login(request):
    return render(request, 'pages/login.html')


# home page function renders index.html and returns response
def home(request):
    books = BookClass.objects.all()

    book1 = {'book1': books[1]}
    # book2 = {'book2': books[0]}
    # book3 = {'book3': books[2]}
    # book4 = {'book4': books[3]}
    # book5 = {'book5': books[4]}
    # book6 = {'book6': books[5]}
    return render(request, 'pages/index.html', book1)


# find out user choise and redirect to relevant page.
def user_choise(request):
    if 'yes_enter' in request.POST:
        return render(request, 'pages/inter_book.html')
    elif 'no_enter' in request.POST:
        return render(request, 'pages/not_inter_book.html')


# our user_chose page view
def result1(request):
    books = pd.read_csv("bookworm_data.csv")

    if 'book1_name' in request.POST:
        bn = request.POST['book1_name'].upper()
    else:
        bn = ""
    if 'book1_type' in request.POST:
        bt = request.POST['book1_type'].upper()
    else:
        bt = ""

    if 'book2_name' in request.POST:
        bn2 = request.POST['book2_name'].upper()
    else:
        bn2 = ""
    if 'book1_type' in request.POST:
        bt2 = request.POST['book2_type'].upper()
    else:
        bt2 = ""

    if 'book3_name' in request.POST:
        bn3 = request.POST['book3_name'].upper()
    else:
        bn3 = ""
    if 'book3_type' in request.POST:
        bt3 = request.POST['book3_type'].upper()
    else:
        bt3 = ""

    if 'book4_name' in request.POST:
        bn4 = request.POST['book4_name'].upper()
    else:
        bn4 = ""
    if 'book4_type' in request.POST:
        bt4 = request.POST['book4_type'].upper()
    else:
        bt4 = ""

    if 'book5_name' in request.POST:
        bn5 = request.POST['book5_name'].upper()
    else:
        bn5 = ""
    if 'book5_type' in request.POST:
        bt5 = request.POST['book5_type'].upper()
    else:
        bt5 = ""
    #  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    books = books.loc[:, ["title", "authors", "isbn",
                          "books_count", "original_publication_year", "average_rating", "image_url", "Genres"]]
    books = books.applymap(lambda s: s.upper() if type(s) == str else s)

    bt.upper()
    bt2.upper()
    bt3.upper()
    bt4.upper()
    bt5.upper()

    if bt == "NONE" and bt2 == "NONE" and bt3 == "NONE" and bt4 == "NONE" and bt5 == "NONE":
        return render(request, 'pages/NameError.html')

    book1 = group(books, bt, 0)
    book2 = group(books, bt2, 1)
    book3 = group(books, bt3, 2)
    book4 = group(books, bt4, 3)
    book5 = group(books, bt5, 4)
    books = []

    if bt != "NONE":
        b1 = OneBook()
        b1.title = book1['title']
        b1.author = book1['authors']
        b1.genres = book1['genres']
        b1.page_num = book1['page_num']
        b1.pub_year = book1['pub_year']
        b1.rating = book1['rating']
        b1.image_url = book1['image_url']
        b1.isbn = book1['isbn']
        books.append(b1)

    if bt2 != "NONE":
        b2 = OneBook()
        b2.title = book2['title']
        b2.author = book2['authors']
        b2.genres = book2['genres']
        b2.page_num = book2['page_num']
        b2.pub_year = book2['pub_year']
        b2.rating = book2['rating']
        b2.image_url = book2['image_url']
        b2.isbn = book2['isbn']
        books.append(b2)

    if bt3 != "NONE":
        b3 = OneBook()
        b3.title = book3['title']
        b3.author = book3['authors']
        b3.genres = book3['genres']
        b3.page_num = book3['page_num']
        b3.pub_year = book3['pub_year']
        b3.rating = book3['rating']
        b3.image_url = book3['image_url']
        b3.isbn = book3['isbn']
        books.append(b3)

    if bt4 != "NONE":
        b4 = OneBook()
        b4.title = book4['title']
        b4.author = book4['authors']
        b4.genres = book4['genres']
        b4.page_num = book4['page_num']
        b4.pub_year = book4['pub_year']
        b4.rating = book4['rating']
        b4.image_url = book4['image_url']
        b4.isbn = book4['isbn']
        books.append(b4)

    if bt5 != "NONE":
        b5 = OneBook()
        b5.title = book5['title']
        b5.author = book5['authors']
        b5.genres = book5['genres']
        b5.page_num = book5['page_num']
        b5.pub_year = book5['pub_year']
        b5.rating = book5['rating']
        b5.image_url = book5['image_url']
        b5.isbn = book5['isbn']
        books.append(b5)

    return render(request, 'pages/result.html', {'books': books})


def result2(request):
    books = pd.read_csv("bookworm_data.csv")

    books = books.loc[:, ["title", "authors", "isbn",
                          "books_count", "original_publication_year", "average_rating", "image_url", "Genres"]]

    books = books.applymap(lambda s: s.upper() if type(s) == str else s)

    if 'personality' in request.POST:
        personality = request.POST['personality'].upper()
    else:
        personality = ""

    if 'age' in request.POST:
        age = request.POST['age'].upper()
    else:
        age = ""

    if 'job' in request.POST:
        job = request.POST['job'].upper()
    else:
        job = ""

    if 'country' in request.POST:
        country = request.POST['country'].upper()
    else:
        country = ""

    # below prints work !!!!!!!!!!
    print(personality)
    print(age)
    print(job)
    print(country)

    # Please select 3 photos from the website as recommendation data(user selected photos for bt1,bt2,bt3)
    # you should enter the book types with capital letters
    bt = "HORROR"
    bt2 = "HISTORY"
    bt3 = "YOUNGADULT"

    group2(books, bt)
    group2(books, bt2)
    group2(books, bt3)

    return render(request, 'pages/NameError.html')
