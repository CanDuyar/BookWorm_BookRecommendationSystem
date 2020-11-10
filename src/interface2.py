#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:50:20 2020

@author: can
"""

#user doesn't have books read before so in this case user will choose one of given booktypes
"""
example scenario:

-Which type is more suitable for you?(Please select one of them...)

*Horror
*Crime
*Science
*History
*Biography
*Classic
*Science Fiction
*Textbook
*Philosophy
*Young Adult
*Travel

As an example, if user selects "Travel" type then we will list Travel books which has 
maximum rating points.


"""
import pandas as pd
import numpy as np
import random


books = pd.read_csv("../data.csv")

books = books.loc[:,["Name","Authors","ISBN","Publisher","Rating"]]


books = books.applymap(lambda s:s.upper() if type(s) == str else s)


    #bt = str(input("Which type of books do you like: ")).upper()
    
number_of_books = books.shape[0]
    
genres = ["Horror","Crime","History","Biography","Classic","Science Fiction","Science"
        ,"Textbook","Philosophy","Young Adult","Travel"]

book_genres = np.zeros([number_of_books],dtype = object)

for x in range(0,number_of_books):
    n = random.randint(0,10)
    book_genres[x] = genres[n].upper()
df = pd.DataFrame(book_genres)
        
def a(bt):
    if bt in df.values:
            
        books["Genres"] = df
        
        gk = books.groupby('Genres') 
        
        #user enters book's type and find books which has this type
        
        number_of_output = 1 # number of books that will print on website
        
        df4 = gk.get_group(bt)
        df5 = df4.groupby('Rating')
        max_rating = max(df5.Rating)
        df6 = df5.get_group(max_rating[0]).head(10)
        print(df6.Name.head(number_of_output).values[0]) # Name Part
        print(df6.ISBN.head(number_of_output).values[0]) # ISBN Part
        print(df6.Publisher.head(number_of_output).values[0]) # Publisher part
        return 0
    

    else:
        print("The Type of Book Doesn't Exist :(" )
        return -1
        

#bt = str(input("Which type of books do you like: ")).upper()
#print(a(bt))
