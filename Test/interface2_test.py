import unittest
import pandas as pd
import interface2_new

books = pd.read_csv("../Assets/Data.csv")

books = books.loc[:, ["title", "writer", "genres",
                      "page_num", "pub_year", "rating", "isbn", "image_url"]]

books = books.applymap(lambda s: s.upper() if type(s) == str else s)


class test_interface2(unittest.TestCase):
    def test_a(self):
        self.assertAlmostEqual(interface2_new.group(books, "SCIENCE"), 1)

    def test_1(self):
        self.assertAlmostEqual(interface2_new.group(books, "SCIENCEFICTION"), 1)

    def test_2(self):
        self.assertAlmostEqual(interface2_new.group(books, "TRAVEL"), 1)

    def test_3(self):
        self.assertAlmostEqual(interface2_new.group(books, "CLASSIC"), 1)

    def test_4(self):
        self.assertAlmostEqual(interface2_new.group(books, "CRIME"), 1)

    def test_5(self):
        self.assertAlmostEqual(interface2_new.group(books, "YOUNGADULT"), 1)

    def test_6(self):
        self.assertAlmostEqual(interface2_new.group(books, "HISTORY"), 1)

    def test_7(self):
        self.assertAlmostEqual(interface2_new.group(books, "ADVENTURE"), 1)

    def test_9(self):
        self.assertAlmostEqual(interface2_new.group(books, "BIOGRAPHY"), 1)

    def test_10(self):
        self.assertAlmostEqual(interface2_new.group(books, "HORROR"), 1)


if __name__ == '__main__':
    unittest.main()
