import pandas as pd
import numpy as np
import random


def group(books, bt):
    gk = books.groupby('Genres')
    df4 = gk.get_group(bt)

    df5 = df4.groupby('average_rating')

    max_rating = max(df5.average_rating)

    df6 = df5.get_group(max_rating[0])

    for x in range(4):
        print(df6.title.values[x])
        print(df6.authors.values[x])
        print(df6.Genres.values[x])
        print(df6.books_count.values[x])
        print(df6.original_publication_year.values[x])
        print(df6.isbn.values[x])
        print("\n")
    return 1


books = pd.read_csv("bookworm_data.csv")

books = books.loc[:, ["title", "authors", "isbn",
                      "books_count", "original_publication_year", "average_rating", "image_url", "Genres"]]

books = books.applymap(lambda s: s.upper() if type(s) == str else s)

# Please select 3 photos from the website as recommendation data(user selected photos for bt1,bt2,bt3)


# you should enter the book types with capital letters
bt = "HORROR"
bt2 = "HISTORY"
bt3 = "YOUNGADULT"

group(books, bt)
group(books, bt2)
group(books, bt3)
