import pandas as pd
from firebase import firebase
from pages_app.models import OneBook


def read_from_firebase():
    f = firebase.FirebaseApplication('https://bookworm-database-default-rtdb.firebaseio.com', None)
    result1 = f.get('/Part1', None)
    f = firebase.FirebaseApplication('https://bookworm-database-default-rtdb.firebaseio.com', None)
    result2 = f.get('/Part2', None)
    book_list = []

    i = 1
    while i in range(len(result1)):
        book_obj = OneBook()
        book_obj.book_id = i
        book_obj.title = result1[i]["TITLE"]
        book_obj.writer = result1[i]["WRITER"]
        book_obj.genres = result1[i]["GENRES"]
        book_obj.page_num = result1[i]["PAGENUM"]
        book_obj.pub_year = result1[i]["PUBYEAR"]
        book_obj.rating = result1[i]["RATING"]
        book_obj.image_url = result1[i]["IMAGEURL"]
        book_obj.isbn = result1[i]["ISBN"]
        book_list.append(book_obj)
        i += 1

    while i in range(len(result2)):
        book_obj = OneBook()
        book_obj.book_id = i
        book_obj.title = result2[i]["TITLE"]
        book_obj.writer = result2[i]["WRITER"]
        book_obj.genres = result2[i]["GENRES"]
        book_obj.page_num = result2[i]["PAGENUM"]
        book_obj.pub_year = result2[i]["PUBYEAR"]
        book_obj.rating = result2[i]["RATING"]
        book_obj.image_url = result2[i]["IMAGEURL"]
        book_obj.isbn = result2[i]["ISBN"]
        book_list.append(book_obj)
        i += 1
    df = pd.DataFrame([x.as_dict() for x in book_list])
    df = df.sample(frac=1)
    return df
