import pandas as pd
# from pages_app.readFromFirebase import read_from_firebase
# d_frame = read_from_firebase()  # read from firebase API
from pages_app import convert_gen


def group(books, bt):
    if bt[0] == "NONE" and bt[1] == "NONE" and bt[2] == "NONE" and bt[3] == "NONE" and bt[4] == "NONE":
        print("Books Types Could Be Found :( . Please Enter At Least One Valid Booktype...")
        return -1
    index = 0

    for book_type in bt:
        if book_type != "NONE":
            gk = books.groupby('genres')
            df4 = gk.get_group(book_type)
            df5 = df4.groupby('rating')
            max_rating = max(df5.rating)
            df6 = df5.get_group(max_rating[0])

            print(df6.title.values[index])  # title
            print(df6.writer.values[index])  # authors
            print(df6.genres.values[index])  # genres
            print(df6.page_num.values[index])  # pages_number
            print(df6.pub_year.values[index])  # publication year
            print(df6.isbn.values[index])  # isbn
            print("\n")
            index += 1
    return 1
