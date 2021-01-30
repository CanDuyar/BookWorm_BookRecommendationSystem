
def group(books, bt):
    gk = books.groupby('genres')
    df4 = gk.get_group(bt)

    df5 = df4.groupby('rating')

    max_rating = max(df5.rating)

    df6 = df5.get_group(max_rating[0])

    for x in range(4):
        print(df6.title.values[x])
        print(df6.writer.values[x])
        print(df6.genres.values[x])
        print(df6.page_num.values[x])
        print(df6.pub_year.values[x])
        print(df6.isbn.values[x])
        print("\n")
    return 1
