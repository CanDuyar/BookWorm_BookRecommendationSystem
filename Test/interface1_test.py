import unittest
import pandas as pd
import interface1_new
# from pages_app.readFromFirebase import read_from_firebase
# d_frame = read_from_firebase()  # read from firebase API
# books = d_frame
books = pd.read_csv("../Assets/Data.csv")
books = books.loc[:, ["title", "writer", "genres",
                      "page_num", "pub_year", "rating", "isbn", "image_url"]]

books = books.applymap(lambda s: s.upper() if type(s) == str else s)


class test_interface1(unittest.TestCase):
    def test_a(self):
        books_type = ["SCIENCE", "SCIENCEFICTION", "NONE", "TRAVEL", "NONE"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)

    def test_b(self):
        books_type = ["HORROR", "CRIME", "YOUNGADULT", "SCIENCE", "CRIME"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)

    def test_c(self):
        books_type = ["HORROR", "HORROR", "HORROR", "HORROR", "HORROR"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)

    def test_d(self):
        books_type = ["SCIENCE", "SCIENCEFICTION", "NONE", "TRAVEL", "NONE"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)

    def test_e(self):
        books_type = ["BIOGRAPHY", "PHILOSOPHY", "CLASSIC", "HISTORY", "HORROR"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)

    def test_f(self):
        books_type = ["NONE", "NONE", "NONE", "NONE", "NONE"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), -1)

    def test_1(self):
        books_type = ["HISTORY", "HISTORY", "HISTORY", "HISTORY", "HISTORY"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)

    def test_2(self):
        books_type = ["PHILOSOPHY", "PHILOSOPHY", "PHILOSOPHY", "PHILOSOPHY", "PHILOSOPHY"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)

    def test_3(self):
        books_type = ["BIOGRAPHY", "BIOGRAPHY", "BIOGRAPHY", "BIOGRAPHY", "BIOGRAPHY"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)

    def test_4(self):
        books_type = ["CRIME", "CRIME", "CRIME", "CRIME", "CRIME"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)

    def test_5(self):
        books_type = ["TRAVEL", "TRAVEL", "TRAVEL", "TRAVEL", "TRAVEL"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)

    def test_6(self):
        books_type = ["SCIENCE", "SCIENCE", "SCIENCE", "SCIENCE", "SCIENCE"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)

    def test_7(self):
        books_type = ["SCIENCEFICTION", "SCIENCEFICTION", "SCIENCEFICTION", "SCIENCEFICTION", "SCIENCEFICTION"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)

    def test_8(self):
        books_type = ["ADVENTURE", "ADVENTURE", "ADVENTURE", "ADVENTURE", "ADVENTURE"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)

    def test_9(self):
        books_type = ["YOUNGADULT", "YOUNGADULT", "YOUNGADULT", "YOUNGADULT", "YOUNGADULT"]
        self.assertAlmostEqual(interface1_new.group(books, books_type), 1)


if __name__ == '__main__':
    unittest.main()
