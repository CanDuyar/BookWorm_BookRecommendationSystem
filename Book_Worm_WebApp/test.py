from django.shortcuts import render
import pandas as pd
import numpy as np
import random

# our result page view
def result(request):
    bn = request.GET['book_name']
    bt = request.GET['book_type']

    books = pd.read_csv("data.csv")

    books = books.loc[:, ["Name", "Authors", "Rating"]]

    if bn in books.Name.values:

        number_of_books = books.shape[0]
        genres = ["Horror", "Crime", "Science", "History", "Biography", "Classic", "Science Fiction", "Science"
            , "Textbook", "Philosophy", "Young Adult", "Travel"]
        book_genres = np.zeros([number_of_books], dtype=object)

        for x in range(0, number_of_books):
            n = random.randint(0, 11)
            book_genres[x] = genres[n]

        df = pd.DataFrame(book_genres)
        books["Genres"] = df
        gk = books.groupby('Genres')