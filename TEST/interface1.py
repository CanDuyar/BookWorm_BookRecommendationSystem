import pandas as pd
import numpy as np
import random

books = pd.read_csv("../data.csv")

books = books.loc[:,["Name","Authors","ISBN","Publisher","pagesNumber","PublishYear","Rating"]]

books = books.applymap(lambda s:s.upper() if type(s) == str else s)

    #bn = str(input("Enter a book's name: ")).upper()
    #bt = str(input("Enter a book's type: ")).upper()
    
number_of_books = books.shape[0]
        
genres = ["Horror","Crime","Science","History","Biography","Classic","Science Fiction","Science"
        ,"Textbook","Philosophy","Young Adult","Travel"]
        
book_genres = np.zeros([number_of_books],dtype = object)

for x in range(0,number_of_books):
    n = random.randint(0,11)
    book_genres[x] = genres[n].upper()
            
df = pd.DataFrame(book_genres)
books["Genres"] = df    
def a(bn , bt):
    if bn in books.Name.values or bt in books.Genres.values:

        if bt in books.Genres.values:
            gk = books.groupby('Genres') 
            df4 = gk.get_group(bt)
        #user enters book's type and find books which has this type
        
            number_of_output = 1 # number of books that will print on website

            df5 = df4.groupby('Rating')
            max_rating = max(df5.Rating)
            df6 = df5.get_group(max_rating[0]).head(10)
            print(df6.Name.head(number_of_output).values[0]) # Name Part
            print(df6.ISBN.head(number_of_output).values[0]) # ISBN Part
            print(df6.Publisher.head(number_of_output).values[0]) # Publisher part
            print(df6.pagesNumber.head(number_of_output).values[0]) # pagesNumber part
            print(df6.PublishYear.head(number_of_output).values[0]) # pagesNumber part
            return 0
    

    #elif bn not in books.Name.values and bt not in books.Genres.values:
        else:
            print("We couldn't find your book :(")
            return -1
        
    else:
            print("We couldn't find your book :(")  
            return -1  

    #elif bt not in books.Genres.values:
    #    print("The Type of Book You Entered Does not Exist in The Database :(")


# bn = str(input("Enter a book's name: ")).upper()
# bt = str(input("Enter a book's type: ")).upper()
# print(a(bn,bt))