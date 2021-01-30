import pandas as pd
from Assets.firebase import firebase
from pages_app.models import OneBook


def read_from_firebase():
    f = firebase.FirebaseApplication('https://bookworm-database-default-rtdb.firebaseio.com', None)
    result1 = f.get('/Part1', None)
    result2 = f.get('/Part2', None)
    result3 = f.get('/Part3', None)
    result4 = f.get('/Part4', None)
    result5 = f.get('/Part5', None)
    result6 = f.get('/Part6', None)
    result7 = f.get('/Part7', None)
    result8 = f.get('/Part8', None)
    result9 = f.get('/Part9', None)
    result10 = f.get('/Part10', None)
    book_list = []

    for i in range(1, 673):
        book_obj = OneBook()
        book_obj.book_id = result1[i]["ID"]
        book_obj.title = result1[i]["TITLE"]
        book_obj.writer = result1[i]["WRITER"]
        book_obj.genres = result1[i]["GENRES"]
        book_obj.page_num = result1[i]["PAGENUM"]
        book_obj.pub_year = result1[i]["PUBYEAR"]
        book_obj.rating = result1[i]["RATING"]
        book_obj.image_url = result1[i]["IMAGEURL"]
        book_obj.isbn = result1[i]["ISBN"]
        book_list.append(book_obj)

    for i in range(673, 1344):
        book_obj = OneBook()
        book_obj.book_id = result2[i]["ID"]
        book_obj.title = result2[i]["TITLE"]
        book_obj.writer = result2[i]["WRITER"]
        book_obj.genres = result2[i]["GENRES"]
        book_obj.page_num = result2[i]["PAGENUM"]
        book_obj.pub_year = result2[i]["PUBYEAR"]
        book_obj.rating = result2[i]["RATING"]
        book_obj.image_url = result2[i]["IMAGEURL"]
        book_obj.isbn = result2[i]["ISBN"]
        book_list.append(book_obj)

    for i in range(1344, 2016):
        book_obj = OneBook()
        book_obj.book_id = result3[str(i)]["ID"]
        book_obj.title = result3[str(i)]["TITLE"]
        book_obj.writer = result3[str(i)]["WRITER"]
        book_obj.genres = result3[str(i)]["GENRES"]
        book_obj.page_num = result3[str(i)]["PAGENUM"]
        book_obj.pub_year = result3[str(i)]["PUBYEAR"]
        book_obj.rating = result3[str(i)]["RATING"]
        book_obj.image_url = result3[str(i)]["IMAGEURL"]
        book_obj.isbn = result3[str(i)]["ISBN"]
        book_list.append(book_obj)

    for i in range(2017, 2688):
        book_obj = OneBook()
        book_obj.book_id = result4[str(i)]["ID"]
        book_obj.title = result4[str(i)]["TITLE"]
        book_obj.writer = result4[str(i)]["WRITER"]
        book_obj.genres = result4[str(i)]["GENRES"]
        book_obj.page_num = result4[str(i)]["PAGENUM"]
        book_obj.pub_year = result4[str(i)]["PUBYEAR"]
        book_obj.rating = result4[str(i)]["RATING"]
        book_obj.image_url = result4[str(i)]["IMAGEURL"]
        book_obj.isbn = result4[str(i)]["ISBN"]
        book_list.append(book_obj)

    for i in range(2688, 3360):
        book_obj = OneBook()
        book_obj.book_id = result5[str(i)]["ID"]
        book_obj.title = result5[str(i)]["TITLE"]
        book_obj.writer = result5[str(i)]["WRITER"]
        book_obj.genres = result5[str(i)]["GENRES"]
        book_obj.page_num = result5[str(i)]["PAGENUM"]
        book_obj.pub_year = result5[str(i)]["PUBYEAR"]
        book_obj.rating = result5[str(i)]["RATING"]
        book_obj.image_url = result5[str(i)]["IMAGEURL"]
        book_obj.isbn = result5[str(i)]["ISBN"]
        book_list.append(book_obj)
    for i in range(3361, 4034):
        book_obj = OneBook()
        book_obj.book_id = result6[str(i)]["ID"]

        book_obj.title = result6[str(i)]["TITLE"]
        book_obj.writer = result6[str(i)]["WRITER"]
        book_obj.genres = result6[str(i)]["GENRES"]
        book_obj.page_num = result6[str(i)]["PAGENUM"]
        book_obj.pub_year = result6[str(i)]["PUBYEAR"]
        book_obj.rating = result6[str(i)]["RATING"]
        book_obj.image_url = result6[str(i)]["IMAGEURL"]
        book_obj.isbn = result6[str(i)]["ISBN"]
        book_list.append(book_obj)

    for i in range(4034, 4706):
        book_obj = OneBook()
        book_obj.book_id = result7[str(i)]["ID"]
        book_obj.title = result7[str(i)]["TITLE"]
        book_obj.writer = result7[str(i)]["WRITER"]
        book_obj.genres = result7[str(i)]["GENRES"]
        book_obj.page_num = result7[str(i)]["PAGENUM"]
        book_obj.pub_year = result7[str(i)]["PUBYEAR"]
        book_obj.rating = result7[str(i)]["RATING"]
        book_obj.image_url = result7[str(i)]["IMAGEURL"]
        book_obj.isbn = result7[str(i)]["ISBN"]
        book_list.append(book_obj)

    for i in range(4706, 5378):
        book_obj = OneBook()
        book_obj.book_id = result8[str(i)]["ID"]
        book_obj.title = result8[str(i)]["TITLE"]
        book_obj.writer = result8[str(i)]["WRITER"]
        book_obj.genres = result8[str(i)]["GENRES"]
        book_obj.page_num = result8[str(i)]["PAGENUM"]
        book_obj.pub_year = result8[str(i)]["PUBYEAR"]
        book_obj.rating = result8[str(i)]["RATING"]
        book_obj.image_url = result8[str(i)]["IMAGEURL"]
        book_obj.isbn = result8[str(i)]["ISBN"]
        book_list.append(book_obj)

    for i in range(5379, 6049):
        book_obj = OneBook()
        book_obj.book_id = result9[str(i)]["ID"]
        book_obj.title = result9[str(i)]["TITLE"]
        book_obj.writer = result9[str(i)]["WRITER"]
        book_obj.genres = result9[str(i)]["GENRES"]
        book_obj.page_num = result9[str(i)]["PAGENUM"]
        book_obj.pub_year = result9[str(i)]["PUBYEAR"]
        book_obj.rating = result9[str(i)]["RATING"]
        book_obj.image_url = result9[str(i)]["IMAGEURL"]
        book_obj.isbn = result9[str(i)]["ISBN"]
        book_list.append(book_obj)

    for i in range(6052, 6565):
        book_obj = OneBook()
        book_obj.book_id = result10[str(i)]["ID"]
        book_obj.title = result10[str(i)]["TITLE"]
        book_obj.writer = result10[str(i)]["WRITER"]
        book_obj.genres = result10[str(i)]["GENRES"]
        book_obj.page_num = result10[str(i)]["PAGENUM"]
        book_obj.pub_year = result10[str(i)]["PUBYEAR"]
        book_obj.rating = result10[str(i)]["RATING"]
        book_obj.image_url = result10[str(i)]["IMAGEURL"]
        book_obj.isbn = result10[str(i)]["ISBN"]
        book_list.append(book_obj)

    df = pd.DataFrame([x.as_dict() for x in book_list])
    return df
