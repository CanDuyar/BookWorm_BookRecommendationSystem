import pandas as pd


def group(books, bt):
    if bt[0] == "NONE" and bt[1] == "NONE" and bt[2] == "NONE" and bt[3] == "NONE" and bt[4] == "NONE":
        print("Books Types Could Be Found :( . Please Enter At Least One Valid Booktype...")
        return -1;
    index = 0;
    for book_type in bt:
        if book_type != "NONE":
            gk = books.groupby('Genres')
            df4 = gk.get_group(book_type)

            df5 = df4.groupby('average_rating')

            max_rating = max(df5.average_rating)

            df6 = df5.get_group(max_rating[0])

            print(df6.title.values[index])  # title
            print(df6.authors.values[index])  # authors
            print(df6.Genres.values[index])  # genres
            print(df6.books_count.values[index])  # pages_number
            print(df6.original_publication_year.values[index])  # publication year
            print(df6.isbn.values[index])  # isbn
            print("\n")
            index += 1

    return 1


books = pd.read_csv("bookworm_data.csv")

books = books.loc[:, ["title", "authors", "isbn",
                      "books_count", "original_publication_year", "average_rating", "image_url", "Genres"]]

books = books.applymap(lambda s: s.upper() if type(s) == str else s)

book_types = [" ", " ", " ", " ", " "]

# bn = str(input("Enter 1. book's name: ")).upper()
bt = str(input("Enter 1. book's type: ")).upper()
book_types[0] = bt

# bn2 = str(input("Enter 2. book's name: ")).upper()
bt2 = str(input("Enter 2. book's type: ")).upper()
book_types[1] = bt2

# bn3 = str(input("Enter 3. book's name: ")).upper()
bt3 = str(input("Enter 3. book's type: ")).upper()
book_types[2] = bt3

# bn4 = str(input("Enter 4. book's name: ")).upper()
bt4 = str(input("Enter 4. book's type: ")).upper()
book_types[3] = bt4

# bn5 = str(input("Enter 5. book's name: ")).upper()
bt5 = str(input("Enter 5. book's type: ")).upper()
book_types[4] = bt5

group(books, book_types)
