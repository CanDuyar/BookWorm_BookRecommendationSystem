import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import joblib
from sklearn.preprocessing import LabelEncoder
from pages_app.models import OneBook
import random


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


'''
# Dataframedeki virgulleri silme kodu
for i in df.columns:
    for j in range(0,len(df.index)):
        if(isinstance(df[i][j],str) == 1):
            df[i][j] = df[i][j].replace(',', '')
df.to_csv("data.csv")
'''

'''
labelenc = LabelEncoder()
df.genres = labelenc.fit_transform(df.genres)
df.to_csv("lEncodeddata.csv")
'''


def inter_1(df, book_type):
    # df = pd.read_csv("Assets/bookworm_data.csv")  # read from csv
    rate = 5
    df = pd.concat([df[:1], df[1:].sample(frac=1)]).reset_index(drop=True)
    df_pivot = df.pivot(index="book_id", columns="genres", values="rating").fillna(0)
    matrix = csr_matrix(df_pivot.values)
    knn = joblib.load('Assets/knn.h5')
    book_obj = OneBook()
    knn.fit(matrix)
    genre = book_type
    lst = df.index[(df['genres'] == genre) & (df['rating'] == 4)].tolist()
    ind = random.randint(0, len(lst)-1)
    query_index = lst[int(ind)]

    distances, indices = knn.kneighbors(df_pivot.iloc[query_index, :].values.reshape(1, -1), n_neighbors=6)
    i = random.randint(0, 5)

    book_obj.title = df.title[df.title.index[indices.flatten()[i]]]
    book_obj.writer = df.writer[df.title.index[indices.flatten()[i]]]
    book_obj.page_num = df.page_num[df.title.index[indices.flatten()[i]]]
    book_obj.pub_year = df.pub_year[df.title.index[indices.flatten()[i]]]
    book_obj.rating = rate
    book_obj.isbn = df.isbn[df.title.index[indices.flatten()[i]]]
    book_obj.image_url = df.image_url[df.title.index[indices.flatten()[i]]].lower()
    book_obj.genres = convert_genres(book_type)
    return book_obj
