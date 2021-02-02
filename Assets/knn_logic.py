import pandas as pd
from scipy.sparse import csr_matrix
import joblib
from pages_app.models import OneBook
import random
from sklearn.neighbors import NearestNeighbors

def convert_genres(gen):
    if gen == 0:
        return "SCIENCE FICTION"
    elif gen == 1:
        return "CLASSIC"
    elif gen == 2:
        return "PHILOSOPHY"
    elif gen == 3:
        return "BIOGRAPHY"
    elif gen == 4:
        return "YOUNG ADULT"
    elif gen == 5:
        return "TRAVEL"
    elif gen == 6:
        return "CRIME"
    elif gen == 7:
        return "SCIENCE"
    elif gen == 8:
        return "HORROR"
    elif gen == 9:
        return "HISTORY"
    elif gen == 10:
        return "ADVENTURE"

def ml_logic(df, book_type):
    rate = 5
    df_pivot = df.pivot(index="book_id", columns="genres", values="rating").fillna(0)
    matrix = csr_matrix(df_pivot.values)
    knn = NearestNeighbors()
    book_obj = OneBook()
    knn.fit(matrix)
    genre = book_type
    lst = df.index[(df['genres'] == genre) & (df['rating'] == 4)].tolist()
    ind = random.randint(0, len(lst) - 1)
    query_index = lst[int(ind)]
    n_neighbors = 21
    distances, indices = knn.kneighbors(df_pivot.iloc[query_index, :].values.reshape(1, -1), n_neighbors=n_neighbors)
    i = random.randint(0, n_neighbors - 1)

    book_obj.title = df.title[df.title.index[indices.flatten()[i]]]
    book_obj.writer = df.writer[df.title.index[indices.flatten()[i]]]
    book_obj.page_num = df.page_num[df.title.index[indices.flatten()[i]]] + 150
    book_obj.pub_year = df.pub_year[df.title.index[indices.flatten()[i]]]
    book_obj.rating = rate
    book_obj.isbn = df.isbn[df.title.index[indices.flatten()[i]]]
    book_obj.image_url = df.image_url[df.title.index[indices.flatten()[i]]].lower()
    book_obj.genres = convert_genres(df.genres[df.title.index[query_index]])

    return book_obj
