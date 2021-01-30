# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:41:05 2020

@author: JIN_HUSSEIN
"""

import unittest
import pandas as pd
import Test.interface3 as interface3

books = pd.read_csv("../Assets/Data.csv")

books = books.loc[:, ["title", "writer", "genres",
                      "page_num", "pub_year", "rating", "isbn", "image_url"]]

books = books.applymap(lambda s: s.upper() if type(s) == str else s)


class test_interface2(unittest.TestCase):
    def test_a(self):
        self.assertAlmostEqual(interface3.group(books, "SCIENCE"), 1)

    def test_1(self):
        self.assertAlmostEqual(interface3.group(books, "SCIENCEFICTION"), 1)

    def test_2(self):
        self.assertAlmostEqual(interface3.group(books, "TRAVEL"), 1)

    def test_3(self):
        self.assertAlmostEqual(interface3.group(books, "CLASSIC"), 1)

    def test_4(self):
        self.assertAlmostEqual(interface3.group(books, "CRIME"), 1)

    def test_5(self):
        self.assertAlmostEqual(interface3.group(books, "YOUNGADULT"), 1)

    def test_6(self):
        self.assertAlmostEqual(interface3.group(books, "HISTORY"), 1)

    def test_7(self):
        self.assertAlmostEqual(interface3.group(books, "ADVENTURE"), 1)

    def test_8(self):
        self.assertAlmostEqual(interface3.group(books, "NONE"), -1)

    def test_9(self):
        self.assertAlmostEqual(interface3.group(books, "BIOGRAPHY"), 1)

    def test_10(self):
        self.assertAlmostEqual(interface3.group(books, "PHILOSOPHY"), 1)

    def test_11(self):
        self.assertAlmostEqual(interface3.group(books, "ADVENTURE"), 1)


if __name__ == '__main__':
    unittest.main()
