import pandas as pd


def group(books, bt):
    if bt[0] == "NONE" and bt[1] == "NONE" and bt[2] == "NONE" and bt[3] == "NONE" and bt[4] == "NONE":
        print("Books Types Could Be Found :( . Please Enter At Least One Valid BookType...")
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
            print(df6.writer.values[index])  # writer
            print(df6.genres.values[index])  # genres
            print(df6.page_num.values[index])  # pages_number
            print(df6.pub_year.values[index])  # publication year
            print(df6.isbn.values[index])  # isbn
            print("\n")
            index += 1

    return 1


books = pd.read_csv("../Assets/Data.csv")

books = books.loc[:, ["title", "writer", "isbn",
                      "page_num", "pub_year", "rating", "image_url", "genres"]]

books = books.applymap(lambda s: s.upper() if type(s) == str else s)

book_types = [" ", " ", " ", " ", " "]
#
# bn = str(input("Enter 1. book's name: ")).upper()
# bt = str(input("Enter 1. book's type: ")).upper()
# book_types[0] = bt
#
# # bn2 = str(input("Enter 2. book's name: ")).upper()
# bt2 = str(input("Enter 2. book's type: ")).upper()
# book_types[1] = bt2
#
# # bn3 = str(input("Enter 3. book's name: ")).upper()
# bt3 = str(input("Enter 3. book's type: ")).upper()
# book_types[2] = bt3
#
# # bn4 = str(input("Enter 4. book's name: ")).upper()
# bt4 = str(input("Enter 4. book's type: ")).upper()
# book_types[3] = bt4
#
# # bn5 = str(input("Enter 5. book's name: ")).upper()
# bt5 = str(input("Enter 5. book's type: ")).upper()
# book_types[4] = bt5
#
# group(books, book_types)