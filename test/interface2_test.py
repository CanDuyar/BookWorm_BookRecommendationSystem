import unittest
import pandas as pd
import test.interface2_new as interface2_new

books = pd.read_csv("bookworm_data.csv")

books = books.loc[:, ["title", "authors", "isbn",
                      "books_count", "original_publication_year", "average_rating", "image_url", "Genres"]]

books = books.applymap(lambda s: s.upper() if type(s) == str else s)


class test_interface2(unittest.TestCase):
    def test_a(self):
        self.assertAlmostEqual(interface2_new.group(books, "SCIENCE"), 1)
        self.assertAlmostEqual(interface2_new.group(books, "SCIENCEFICTION"), 1)
        self.assertAlmostEqual(interface2_new.group(books, "TRAVEL"), 1)
        self.assertAlmostEqual(interface2_new.group(books, "CLASSIC"), 1)
        self.assertAlmostEqual(interface2_new.group(books, "CRIME"), 1)


if __name__ == '__main__':
    unittest.main()
