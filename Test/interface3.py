# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:26:06 2020

@author: JIN_HUSSEIN
"""


def group(books, bt):
    if bt == "NONE":
        print("Error: Choose At least One Type Of Book 🙂\n")
        return -1
    gk = books.groupby('genres')
    df4 = gk.get_group(bt)

    df5 = df4.groupby('rating')

    max_rating = max(df5.rating)

    df6 = df5.get_group(max_rating[0])

    for x in range(20):
        print(df6.title.values[x])
        print(df6.writer.values[x])
        print(df6.genres.values[x])
        print(df6.page_num.values[x])
        print(df6.pub_year.values[x])
        print(df6.isbn.values[x])
        print("\n")
    return 1

