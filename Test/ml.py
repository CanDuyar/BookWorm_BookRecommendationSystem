import unittest
import pandas as pd
from Assets import knn_logic

from django.conf import settings

settings.configure(DEBUG=True)

# from pages_app.readFromFirebase import read_from_firebase
#
# d_frame = read_from_firebase()  # read from firebase API
d_frame = books = pd.read_csv("../Assets/DataSet.csv")


# books = d_frame.loc[:, ["title", "book_id", "writer", "genres",
#                       "page_num", "pub_year", "rating", "isbn", "image_url"]]
#
# books = books.applymap(lambda s: s.upper() if type(s) == str else s)


class test_ml_logic(unittest.TestCase):
    def test_a(self):
        self.assertAlmostEqual(knn_logic.ml_logic(d_frame, 0).genres, "SCIENCE FICTION")

    def test_a1(self):
        self.assertAlmostEqual(knn_logic.ml_logic(d_frame, 1).genres, "CLASSIC")

    def test_a2(self):
        self.assertAlmostEqual(knn_logic.ml_logic(d_frame, 2).genres, "PHILOSOPHY")

    def test_a3(self):
        self.assertAlmostEqual(knn_logic.ml_logic(d_frame, 3).genres, "BIOGRAPHY")

    def test_a4(self):
        self.assertAlmostEqual(knn_logic.ml_logic(d_frame, 4).genres, "YOUNG ADULT")

    def test_a5(self):
        self.assertAlmostEqual(knn_logic.ml_logic(d_frame, 5).genres, "TRAVEL")

    def test_a6(self):
        self.assertAlmostEqual(knn_logic.ml_logic(d_frame, 6).genres, "CRIME")

    def test_a7(self):
        self.assertAlmostEqual(knn_logic.ml_logic(d_frame, 7).genres, "SCIENCE")

    def test_a8(self):
        self.assertAlmostEqual(knn_logic.ml_logic(d_frame, 8).genres, "HORROR")

    def test_a9(self):
        self.assertAlmostEqual(knn_logic.ml_logic(d_frame, 9).genres, "HISTORY")

    def test_a10(self):
        self.assertAlmostEqual(knn_logic.ml_logic(d_frame, 10).genres, "ADVENTURE")


if __name__ == '__main__':
    unittest.main()
