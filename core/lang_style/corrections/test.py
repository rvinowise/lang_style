import unittest
import sys

from .corrections import Corrections


class MyTestCase(unittest.TestCase):

    def test_something(self):
        corrections = Corrections()
        corrections.word_choices.extend(["lol", "lolius"])
        print(str(corrections))

