from django.shortcuts import render
import pandas as pd
import numpy as np
import random
from pages_app.models import BookClass


# our home page view

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


# our user_choise page view
def result(request):
    books = pd.read_csv("data.csv")

    if 'no_enter' in request.GET:

        books = books.loc[:, ["Name", "Authors", "ISBN", "Publisher", "pagesNumber", "PublishYear", "Rating"]]
        books = books.applymap(lambda s: s.upper() if type(s) == str else s)

        # Get Users Information
        #  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

        #  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # this part should be changed according to upper values from user.

        bt = request.GET['cars'].upper()
        number_of_books = books.shape[0]

        genres = ["Horror", "Crime", "History", "Biography", "Classic", "Science Fiction", "Science"
            , "Textbook", "Philosophy", "Young Adult", "Travel"]

        book_genres = np.zeros([number_of_books], dtype=object)

        for x in range(0, number_of_books):
            n = random.randint(0, 10)
            book_genres[x] = genres[n].upper()

        df = pd.DataFrame(book_genres)

        if bt in df.values:

            books["Genres"] = df

            gk = books.groupby('Genres')

            # user enters book's type and find books which has this type

            number_of_output = 1  # number of books that will print on website

            df4 = gk.get_group(bt)
            df5 = df4.groupby('Rating')
            max_rating = max(df5.Rating)
            df6 = df5.get_group(max_rating[0]).head(number_of_output)

            book1_name = df6.Name.head(number_of_output).values[0]
            book_writer_name = df6.Authors.head(number_of_output).values[0]
            book_isbn = df6.ISBN.head(number_of_output).values[0]
            book_publisher = df6.Publisher.head(number_of_output).values[0]
            book_rating = df6.Rating.head(number_of_output).values[0]
            book_page_num = df6.pagesNumber.head(number_of_output).values[0]
            book_pub_year = df6.PublishYear.head(number_of_output).values[0]
            book_genres = df6.Genres.head(number_of_output).values[0]

            return render(request, 'pages/result.html',
                          {'book1_name': book1_name, 'book_genres': book_genres, 'book_writer_name': book_writer_name,
                           'book_isbn': book_isbn, 'book_publisher': book_publisher, 'book_rating': book_rating,
                           'book_page_num': book_page_num, 'book_pub_year': book_pub_year})
        else:
            return render(request, 'pages/TypeError.html', {'bt': bt})

    # If User Enters Some Books
    else:

        books = books.loc[:, ["Name", "Authors", "ISBN", "Publisher", "pagesNumber", "PublishYear", "Rating"]]
        books = books.applymap(lambda s: s.upper() if type(s) == str else s)

        # Get Books Names And Types
        #  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

        number_of_books = books.shape[0]

        genres = ["Horror", "Crime", "Science", "History", "Biography", "Classic", "Science Fiction", "Science"
            , "Textbook", "Philosophy", "Young Adult", "Travel"]

        book_genres = np.zeros([number_of_books], dtype=object)

        for x in range(0, number_of_books):
            n = random.randint(0, 11)
            book_genres[x] = genres[n].upper()

        df = pd.DataFrame(book_genres)
        books["Genres"] = df

        if bn in books.Name.values or bt in books.Genres.values:

            if bt in books.Genres.values:
                gk = books.groupby('Genres')
                df4 = gk.get_group(bt)
                # user enters book's type and find books which has this type
                number_of_output = 1  # number of books that will print on website

                df5 = df4.groupby('Rating')
                max_rating = max(df5.Rating)

                df6 = df5.get_group(max_rating[0]).head(number_of_output)
                book_name = df6.Name.head(number_of_output).values[0]
                book_writer_name = df6.Authors.head(number_of_output).values[0]
                book_isbn = df6.ISBN.head(number_of_output).values[0]
                book_publisher = df6.Publisher.head(number_of_output).values[0]
                book_rating = df6.Rating.head(number_of_output).values[0]
                book_page_num = df6.pagesNumber.head(number_of_output).values[0]
                book_pub_year = df6.PublishYear.head(number_of_output).values[0]
                book_genres = df6.Genres.head(number_of_output).values[0]

                return render(request, 'pages/result.html',
                              {'book_name': book_name, 'book_genres': book_genres, 'book_writer_name': book_writer_name,
                               'book_isbn': book_isbn, 'book_publisher': book_publisher, 'book_rating': book_rating,
                               'book_page_num': book_page_num, 'book_pub_year': book_pub_year})
            # elif bn not in books.Name.values and bt not in books.Genres.values:
            else:
                return render(request, 'pages/NameError.html', {'bn': bn, 'bt': bt})
        else:
            return render(request, 'pages/NameError.html', {'bn': bn, 'bt': bt})
