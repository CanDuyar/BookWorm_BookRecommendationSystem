import unittest
import pandas as pd
import interface1_new

books = pd.read_csv("../Assets/Data.csv")

books = books.loc[:, ["title", "writer", "isbn",
                      "page_num", "pub_year", "rating", "image_url", "genres"]]

books = books.applymap(lambda s: s.upper() if type(s) == str else s)


class test_interface1(unittest.TestCase):
    def test_a(self):
        books_type = ["HORROR", "CRIME", "YOUNGADULT", "SCIENCE", "NONE"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)
        books_type = ["HORROR", "CRIME", "YOUNGADULT", "SCIENCE", "CRIME"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)
        books_type = ["HORROR", "HORROR", "HORROR", "HORROR", "HORROR"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)
        books_type = ["SCIENCE", "SCIENCEFICTION", "TEXTBOOK", "TRAVEL", "HISTORY"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)
        books_type = ["BIOGRAPHY", "PHILOSOPHY", "CLASSIC", "NONE", "HISTORY"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)
        books_type = ["NONE", "NONE", "NONE", "NONE", "NONE"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), -1)


if __name__ == '__main__':
    unittest.main()
